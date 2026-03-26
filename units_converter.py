#!/usr/bin/env python3
"""Units Converter - Convert between common units of measurement."""

import argparse

CONVERSIONS = {
    # Length (base: meter)
    "km": ("length", 1000),
    "m": ("length", 1),
    "cm": ("length", 0.01),
    "mm": ("length", 0.001),
    "mile": ("length", 1609.344),
    "yard": ("length", 0.9144),
    "foot": ("length", 0.3048),
    "inch": ("length", 0.0254),
    # Weight (base: kilogram)
    "kg": ("weight", 1),
    "g": ("weight", 0.001),
    "mg": ("weight", 1e-6),
    "lb": ("weight", 0.453592),
    "oz": ("weight", 0.0283495),
    # Temperature handled separately
    # Volume (base: liter)
    "l": ("volume", 1),
    "ml": ("volume", 0.001),
    "gallon": ("volume", 3.78541),
    "quart": ("volume", 0.946353),
    "pint": ("volume", 0.473176),
    "cup": ("volume", 0.236588),
    "fl_oz": ("volume", 0.0295735),
}


def convert_temperature(value: float, from_unit: str, to_unit: str) -> float:
    # Convert to Celsius first
    if from_unit == "c":
        celsius = value
    elif from_unit == "f":
        celsius = (value - 32) * 5 / 9
    elif from_unit == "k":
        celsius = value - 273.15
    else:
        raise ValueError(f"Unknown temperature unit: {from_unit}")

    if to_unit == "c":
        return celsius
    elif to_unit == "f":
        return celsius * 9 / 5 + 32
    elif to_unit == "k":
        return celsius + 273.15
    else:
        raise ValueError(f"Unknown temperature unit: {to_unit}")


def convert(value: float, from_unit: str, to_unit: str) -> float:
    from_unit = from_unit.lower()
    to_unit = to_unit.lower()

    temp_units = {"c", "f", "k"}
    if from_unit in temp_units or to_unit in temp_units:
        return convert_temperature(value, from_unit, to_unit)

    if from_unit not in CONVERSIONS:
        raise ValueError(f"Unknown unit: {from_unit}")
    if to_unit not in CONVERSIONS:
        raise ValueError(f"Unknown unit: {to_unit}")

    from_cat, from_factor = CONVERSIONS[from_unit]
    to_cat, to_factor = CONVERSIONS[to_unit]

    if from_cat != to_cat:
        raise ValueError(f"Cannot convert {from_unit} ({from_cat}) to {to_unit} ({to_cat})")

    return value * from_factor / to_factor


def main():
    parser = argparse.ArgumentParser(description="Convert between units")
    parser.add_argument("value", type=float, help="Value to convert")
    parser.add_argument("from_unit", help="Source unit (e.g. km, lb, c)")
    parser.add_argument("to_unit", help="Target unit (e.g. mile, kg, f)")
    args = parser.parse_args()

    result = convert(args.value, args.from_unit, args.to_unit)
    print(f"{args.value} {args.from_unit} = {result:.6g} {args.to_unit}")


if __name__ == "__main__":
    main()
