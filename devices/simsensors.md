# Simsensors

Simsensors (simulated sensors) are a set of tools designed to facilitate the mocking of data from physical sensors
during software development and testing. It provides a flexible and configurable environment to simulate sensor
readings, allowing developers to mimic various sensor behaviours without relying on actual hardware.

The concrete implementation of the Simsensor publishes prepared measurement readings from a special file.

## Supported sensors

Currently, all types of sensors supported by sensorhub have their simulated type. The naming convention
assumes the use
of the `_sim` suffix, for example, `baro_sim` for the barometer.

## File format

The concrete simulated sensor needs a special `CSV` file, which contains measurements saved in table structured format.

### Columns

- The first column contains the ID of a sensor type, which corresponds to IDs from sensorhub. The first
column contains the ID of a sensor type, which corresponds to the IDs from Sensorhub. Furthermore, as described in the
[Timestamps logic](#timestamps-logic) section, the end scenario indicator can be used as a value of this field.
All currently available values are listed below.

| Sensor type   | ID |
| ------------- | -- |
| End scenario  |  0 |
| Accelerometer |  1 |
| Barometer     |  2 |
| GPS           |  4 |
| Gyroscope     |  8 |
| Magnetometer  | 16 |
| Thermometer   | 32 |

- The second column contains a timestamp of a particular measurement. The timestamp should be in **milliseconds**.
It is important to note that it does not have to be a real-time timestamp. The precise meaning of a timestamp
is described in the section [Timestamps logic](#timestamps-logic).

- In consecutive columns, measurement results are stored. Depending on a particular sensor type meaning of a particular
column can be different. Below all the possibilities are described.

#### Accelerometer

 1. Acceleration along `X` axis [mm/s²]
 1. Acceleration along `Y` axis [mm/s²]
 1. Acceleration along `Z` axis [mm/s²]

#### Barometer

 1. Pressure in Pascals [Pa]
 1. Temperature in Kelvins [K]

#### GPS

 1. Altitude above MSL [mm]
 1. Latitude in nanodegrees [ndeg]
 1. Longitude in nanodegrees [ndeg]
 1. GPS UTC time in microseconds [us]
 1. Horizontal dilution of precision
 1. Vertical dilution of precision
 1. Altitude above Ellipsoid [mm]
 1. GPS ground speed [mm/s]
 1. GPS North velocity [mm/s]
 1. GPS East velocity [mm/s]
 1. GPS Down velocity [mm/s]
 1. GPS horizontal position accuracy [mm]
 1. GPS vertical position accuracy [mm]
 1. GPS velocity accuracy [mm]
 1. Heading [mrad]
 1. Heading offset [mrad]
 1. Heading accuracy [mrad]
 1. Number of used satellites
 1. Fix quality

#### Gyroscope

 1. Angular velocity value along `X` axis [mrad/s]
 1. Angular velocity value along `Y` axis [mrad/s]
 1. Angular velocity value along `Z` axis [mrad/s]
 1. Delta angle in [urad] since driver start along `X` axis
 1. Delta angle in [urad] since driver start along `Y` axis
 1. Delta angle in [urad] since driver start along `Z` axis

#### Magnetometer

 1. Value along X axis in 1E-7 [T]
 1. Value along Y axis in 1E-7 [T]
 1. Value along Z axis in 1E-7 [T]

#### Thermometer

 1. Temperature value in Kelvin [K]

### Header row

The first row **can** be a header, which describes the meaning of particular columns. Structure of a header is shown
below.

```console
SensorID,Timestamp,Fld1,Fld2, ...
```

First two columns - `SensorID` and `Timestamp` are mandatory. The rest of header columns are optional. Value of these
fields is not specified.

### Timestamps logic

Timestamps from file represents the time delays between subsequent measurements. Precise algorithm:

 1. Read first measurement and publish it with current time,
 1. Read next measurement and calculate offset between actual and previous timestamp from file,
 1. Wait for offset milliseconds,
 1. Publish measurement with timestamp equal to previously published timestamp plus offset.

It is undefined behavior, when previous timestamp is bigger than the current one. In file, they should be sorted in not
descending order.

### Ending and looping scenario

By default, when simsonsor encounter last measurement in a file, then it goes to the beginning of the file and repeats
reading all measurements. Timestamps monotonicity is preserved. Time span between the last reading and the first one
from file is considered to be equal to 0. In practice the time between publishes is as small as possible.

It is also possible to end the scenario. For this purpose special end scenario indicator - `0` should be placed in
first column (as described in [this section](#columns)). Simsensor doesn't publish any new events after this symbol.

### File example

```console
SensorID,Timestamp,Field1,Field2,Field3
1,2282607175,748,-419,-9780,0
8,2282607175,-2,-64,0,0
1,2282610344,740,-484,-9776,0
8,2282610344,-6,-71,-2,0
1,2282612689,740,-484,-9776,0
8,2282612689,-6,-73,-3,0
1,2282614538,742,-510,-9788,0
8,2282614538,-1,-68,-2,0
1,2282617192,723,-517,-9783,0
```

## Usage

Running selected Simsensor is analogical to start collecting data from a physical device. There is only one required
argument: the path to a file containing the measurement scenario to be used. Command to start sensor should look file
this:

```console
./sbin/sensors -s <sensor_type>_sim:<scenario_file_path>
```

From perspective of data consumer, nothing changes.

### Starting simsensor

Assume that mocking barometer data is needed and path to file with data to be published is
`./etc/mock_measurements.csv`. Then the command to start looks like this:

```console
./sbin/sensors -s baro_sim:./etc/mock_measurements.csv
```
