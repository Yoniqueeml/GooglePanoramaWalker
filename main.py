from concurrent.futures import ThreadPoolExecutor
from PathFinder import get_path
from SearchPanorama import search_panoramas
from DownloadPanorama import get_panorama


def download_panorama(i, coordinates):
    pan_id = search_panoramas(coordinates[1], coordinates[0])

    if pan_id == [] or not pan_id:
        return

    pan_view = get_panorama(pan_id[-1].pano_id)
    pan_view.save(f'image{i}.jpg', 'jpeg')


def walk(startPoint: str, endPoint: str):
    path = get_path(startPoint, endPoint)
    print(path)

    with ThreadPoolExecutor(max_workers=5) as executor:
        futures = []

        for i, coordinates in enumerate(path):
            future = executor.submit(download_panorama, i, coordinates)
            futures.append(future)

        for future in futures:
            future.result()


import time

if __name__ == "__main__":
    start_time = time.time()
    walk("Московское шоссе 145", "Ново-Вокзальная 215")
    end_time = time.time()
    elapsed_time = end_time - start_time
    print('Elapsed time: ', elapsed_time)
