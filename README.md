# Units Converter

A Python CLI tool to convert between common units: length, weight, volume, and temperature.

## Installation

```bash
git clone https://github.com/Al-Muaalemi/units-converter.git
cd units-converter
python units_converter.py --help
```

No external dependencies — uses Python standard library only.

## Usage

```bash
python units_converter.py <value> <from_unit> <to_unit>
```

### Examples

```bash
# Length
python units_converter.py 10 km mile

# Weight
python units_converter.py 70 kg lb

# Temperature
python units_converter.py 100 c f

# Volume
python units_converter.py 2 gallon l
```

## Supported Units

| Category | Units |
|----------|-------|
| Length | km, m, cm, mm, mile, yard, foot, inch |
| Weight | kg, g, mg, lb, oz |
| Temperature | c, f, k |
| Volume | l, ml, gallon, quart, pint, cup, fl_oz |
