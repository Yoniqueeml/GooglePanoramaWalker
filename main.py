from concurrent.futures import ThreadPoolExecutor
from utils.PathFinder import get_path
from utils.DownloadPanorama import download_gopanorama
from utils.yandex import download_yapanorama


def walk_google(startPoint: str, endPoint: str):
    path = get_path(startPoint, endPoint)
    print(path)

    with ThreadPoolExecutor(max_workers=5) as executor:
        futures = []

        for i, coordinates in enumerate(path):
            future = executor.submit(download_gopanorama, i, coordinates)
            futures.append(future)

        for future in futures:
            future.result()


def walk_yandex(startPoint: str, endPoint: str):
    path = get_path(startPoint, endPoint)
    print(path)
    download_yapanorama(path)


import time

if __name__ == "__main__":
    start_time = time.time()
    walk_yandex("Московское шоссе 145", "Ново-Вокзальная 215")
    end_time = time.time()
    elapsed_time = end_time - start_time
    print('Elapsed time: ', elapsed_time)
