from PathFinder import get_path
from SearchPanorama import search_panoramas
from DownloadPanorama import download_panorama


def walk(startPoint: str, endPoint: str):
    path = get_path(startPoint, endPoint)
    for i in range(len(path)):
        pan_id = search_panoramas(path[i][0], path[i][1])
        pan_view = download_panorama(pan_id)
        pan_view.save(f'image{i}.jpg', 'jpeg')