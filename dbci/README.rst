Database Cache Indexer
======================


.. code-block:: yaml

    name: tudat

    # Define files
    - name: SpaceData/SW-Last5Years.txt
    type: file
    url: http://www.celestrak.com/SpaceData/SW-Last5Years.txt

    - name: Default
    type: zip
    remote_url: https://www.filehosting.org/file/details/886116/resource.zip

    # Defines compressed files to be downloaded and uncompressed.
    - name: gravity_models/egm96
    type: z
    remote_url: https://earth-info.nga.mil/GandG/wgs84/gravitymod/egm96/egm96.z

    - name: gravity_models/egm96
    type: z
    remote_url: https://earth-info.nga.mil/GandG/wgs84/gravitymod/egm96/egm96.z

    # For simplified acquisition of further resources.
    - name: NASA-NAIF
    type: page
    remote_url: https://naif.jpl.nasa.gov/pub/naif/

    - name: CelesTrak
    type: page
    remote_url: http://www.celestrak.com/