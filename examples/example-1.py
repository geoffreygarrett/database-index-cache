"""example-1.py
[`tudat`](https://github.com/tudat-team/tudat) is a platform to perform astrodynamics and space research. At the core of
the library is the use of remote resources such as ephemeris data (tabulated position data of celestial objects),
atmosphere models and space weather data for simulation dynamics.
"""

from idc import DataManager

if __name__ == "__main__":
    # inheritance and definition of default config file path in tudat source
    class TudatData(DataManager):
        default_config_path = "example-1.yaml"


    # create default tudat resources
    asset_manager = TudatData.default()

    # download all targeted assets
    asset_manager.download_targets(parallel=False)

    # export the download cache to a zip file
    asset_manager.export_download_cache("example-1.zip", overwrite=True)

    # check download cache size
    print(f"{asset_manager.cache_total_size() / 1E6} MB")

    # clear the cache located in ~/.tudat/cache (unix)
    # asset_manager.clear_download_cache()

    # check download cache size
    print(f"{asset_manager.cache_total_size() / 1E6} MB")

    # import cache
    asset_manager.import_download_cache("example-1.zip")

    # clear the cache located in ~/.tudat/cache (unix)
    # asset_manager.clear_download_cache()

    # retrieve path to celestrak stations tle
    data_file_paths = [
        asset_manager["celestrak/tle/stations.txt"],  # file type
        asset_manager["gravity_models/egm96/EGM96"],  # archive type
        asset_manager["celestrak/space_data/SW-Last5Years.txt"]]  # route type

    for p in data_file_paths:
        print(p)

    # # From here, there are a few use case scenarios
    # class Cases(Enum):
    #     cache_targets = 0  # download all listed target assets
    #     clear_cache = 1  # remove all listed assets
    #     record = 2  # record the use of assets
    #     archive = 3  # archive all resources into zip
    #     request = 4  # request a specific resource
    #
    #
    # #
    # for case in Cases:
    #     if case == Cases.cache_targets:
    #         asset_manager.cache_targets()
    #
    #     elif case == Cases.clear_cache:
    #         print(asset_manager.cache_total_size())
    #         # asset_manager.clear_cache()
    #
    #     elif case == Cases.record:
    #         # start a clear asset usage record
    #         pass
    #         # asset_manager.start_record("example-1-record")
    #         #
    #         # # use specific asset files
    #         # _ = asset_manager["celestrak/tle/txt/stations.txt"]
    #         # _ = asset_manager["celestrak/tle/txt/tle-new.txt"]
    #         #
    #         # # retrieve list of used assets
    #         # record = asset_manager.save_record(clear=True)
    #
    #     elif case == Cases.archive:
    #         pass
    #         # archive cache
    #         # asset_manager.archive_cache("example-1")
    #
    #     # elif case == Cases.request:
