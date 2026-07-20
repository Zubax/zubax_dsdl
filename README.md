# Zubax Cyphal DSDL

Public unregulated vendor-specific [Cyphal](https://opencyphal.org) DSDL definitions.

Related tools:

- [PyDSDL](https://github.com/OpenCyphal/pydsdl) -- parse, serialize, and deserialize DSDL in Python.
- [Nunavut](https://github.com/OpenCyphal/nunavut) -- generate DSDL serialization code in various languages.
- [llvm-dsdl](https://github.com/OpenCyphal-Garage/llvm-dsdl) -- DSDL codegen based on LLVM.

Conventions:

- For world fixed frames, the North-East-Down (NED) right-handed notation is preferred:
  X – northward, Y – eastward, Z – downward.

- In relation to a body, the convention is as follows, right-handed:
  X – forward, Y – rightward, Z – downward.

- Angular velocities are represented using the right-handed, fixed-axis (extrinsic) convention:
  X (roll), Y (pitch), Z (yaw).

- For NED frames, the initial (zero) rotation of a body is the state where the axes of the body frame are
  aligned with the axes of the local NED frame: X points north, Y points east, Z points down.

- Matrices are represented in the row-major order.
