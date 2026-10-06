#!/usr/bin/env python3
"""
PyAEDT Automation Script for 5 GHz Inset-Fed Microstrip Patch Antenna
Author: Tanmay Kumar (IEEE Techblocks RF and Antenna Simulation Capstone)

This script automates the creation and simulation setup of the 5 GHz Inset-Fed
Patch Antenna in Ansys Electronics Desktop / HFSS using PyAEDT.

Prerequisites:
    pip install pyaedt
"""

import sys

try:
    from pyaedt import Hfss
except ImportError:
    print("[NOTE] pyaedt is not installed in the current environment.")
    print("To run this automation script in Ansys HFSS, install pyaedt via: pip install pyaedt")


def build_5ghz_patch(project_name="Patch_5GHz_Perfect", design_name="InsetPatch", non_graphical=False):
    """Creates the 5 GHz patch antenna in HFSS with exact capstone parameters."""
    print(f"Initializing HFSS session for {design_name}...")
    hfss = Hfss(
        projectname=project_name,
        designname=design_name,
        solution_type="DrivenModal",
        new_desktop_session=True,
        non_graphical=non_graphical
    )

    hfss.modeler.model_units = "mm"

    # Define Design Variables
    variables = {
        "h_s": "1.6mm",          # Substrate height
        "h_m": "0.035mm",        # Copper thickness (1 oz)
        "w_p": "18.2574mm",      # Patch width
        "l_p": "13.6629mm",      # Patch length
        "w_f": "3.059mm",        # 50 Ohm Feedline width
        "y_0": "4.6689mm",       # Inset notch depth (tuned for 50 Ohm)
        "g": "0.5mm",            # Inset notch gap
        "w_s": "w_p + 6 * h_s",  # Substrate width
        "l_s": "l_p + 6 * h_s",  # Substrate length
    }

    for var_name, var_val in variables.items():
        hfss[var_name] = var_val

    # 1. Create Ground Plane
    print("Creating Ground Plane...")
    hfss.modeler.create_box(
        position=["-w_s/2", "-l_s/2", "-h_s"],
        dimensions_list=["w_s", "l_s", "-h_m"],
        name="Ground",
        matname="copper"
    )

    # 2. Create Substrate (FR4_epoxy)
    print("Creating FR-4 Substrate...")
    hfss.modeler.create_box(
        position=["-w_s/2", "-l_s/2", "-h_s"],
        dimensions_list=["w_s", "l_s", "h_s"],
        name="Substrate",
        matname="FR4_epoxy"
    )

    # 3. Create Main Patch
    print("Creating Patch and Inset Feed...")
    patch = hfss.modeler.create_box(
        position=["-w_p/2", "-l_p/2", "0mm"],
        dimensions_list=["w_p", "l_p", "h_m"],
        name="Patch_Body",
        matname="copper"
    )

    # Inset Cutouts (Slots)
    slot1 = hfss.modeler.create_box(
        position=["-w_f/2 - g", "-l_p/2", "0mm"],
        dimensions_list=["g", "y_0", "h_m"],
        name="Slot_Left",
        matname="vacuum"
    )
    slot2 = hfss.modeler.create_box(
        position=["w_f/2", "-l_p/2", "0mm"],
        dimensions_list=["g", "y_0", "h_m"],
        name="Slot_Right",
        matname="vacuum"
    )

    # Subtract notches from patch body
    hfss.modeler.subtract(blank_list=[patch.name], tool_list=[slot1.name, slot2.name], keep_originals=False)

    # 4. Create Microstrip Feedline
    feed_len = "(l_s - l_p)/2 + y_0"
    feed = hfss.modeler.create_box(
        position=["-w_f/2", "-l_s/2", "0mm"],
        dimensions_list=["w_f", feed_len, "h_m"],
        name="Feedline",
        matname="copper"
    )

    # Unite Patch and Feedline
    hfss.modeler.unite(assignment=[patch.name, feed.name])

    # 5. Create Lumped Port Sheet
    print("Creating Port Sheet...")
    port_sheet = hfss.modeler.create_rectangle(
        orientation="XZ",
        origin=["-w_f/2", "-l_s/2", "-h_s"],
        sizes=["w_f", "h_s"],
        name="PortSheet"
    )

    # Assign Lumped Port with Integration Line
    hfss.lumped_port(
        assignment=port_sheet.name,
        integration_line=[["0mm", "-l_s/2", "-h_s"], ["0mm", "-l_s/2", "0mm"]],
        port_name="1",
        impedance=50.0
    )

    # 6. Radiation Air Box
    print("Creating Radiation AirBox and Rad1 boundary...")
    airbox = hfss.modeler.create_box(
        position=["-w_s", "-l_s", "-h_s - 15mm"],
        dimensions_list=["2*w_s", "2*l_s", "h_s + 45mm"],
        name="AirBox",
        matname="air"
    )
    hfss.assign_radiation_boundary_to_faces(assignment=airbox.faces, boundary_name="Rad1")

    # 7. Analysis Setup (Setup1: 5 GHz, Max 20 Passes, Delta S = 0.01)
    print("Configuring Analysis Setup...")
    setup = hfss.create_setup(name="Setup1", setup_type="HfssDriven")
    setup.props["Frequency"] = "5GHz"
    setup.props["MaximumPasses"] = 20
    setup.props["MaxDeltaS"] = 0.01

    # Frequency Sweep (4 GHz to 6 GHz, Interpolating)
    setup.create_frequency_sweep(
        unit="GHz",
        sweep_type="Interpolating",
        start_frequency=4.0,
        stop_frequency=6.0,
        step_size=0.01,
        name="Sweep"
    )

    # Save Project
    hfss.save_project()
    print("Model successfully built and saved!")
    return hfss


if __name__ == "__main__":
    if "pyaedt" in sys.modules:
        build_5ghz_patch(non_graphical=True)
    else:
        print("Run with PyAEDT installed in an Ansys-compatible Python environment.")
