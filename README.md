Hi everyone. I spent some time working on a download-cacher/resource-manager/index-cacher tudat/tudatpy (to be honest, I have no idea what it's
called, and I can't find any existing solution for solution)

The goal of decoupling all data files from the packages. The idea has the following components.

Configuration yaml

````yaml
name: tudat  # => assets will be cached in ~/.tudat

assets:
  - name: SpaceData/SW-Last5Years.txt
    url: http://www.celestrak.com/SpaceData/SW-Last5Years.txt

  - name: NAIF
    url: https://naif.jpl.nasa.gov/pub/naif/

  - name: default
    url: https://www.testing/resource.zip
````

Ok so let's break this down:

Assets can be of the types:
website indexes, such as NASA-NAIF's public data repository for spice.

````yaml
   - name: NASA-NAIF
     url: https://naif.jpl.nasa.gov/pub/naif/
````

files, such as txt data from Celestrak.

````yaml
   - name: SpaceData/SW-Last5Years.txt
     url: http://www.celestrak.com/SpaceData/SW-Last5Years.txt
````

compressed, such as the legacy tudat data.

````yaml
   - name: default
     url: https://www.testing/resource.zip
````

The asset configuration can be loaded into code as:

````python
from dbci import IndexClient

index = IndexClient.from_yaml('config.yaml')
de435 = index.NASA["generic_kernels/spk/planets/de435.bsp"]


````

For the case of website indexes:

- name: NASA-NAIF url: https://naif.jpl.nasa.gov/pub/naif/

path = assets.NAIF['/PHOBOS88/kernels/spk/iam2_r2.bsp']

~/.tudat/NAIF/PHOBOS88/kernels/spk/iam2_r2.bsp? Yes: Return path, No: Download - then return path.