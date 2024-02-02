from PathFinder import get_path
from SearchPanorama import search_panoramas
from DownloadPanorama import get_panorama


def walk(startPoint: str, endPoint: str):
    path = get_path(startPoint, endPoint)
    print(path)
    for i in range(len(path)):
        # print(path[i][1], path[i][0])
        pan_id = search_panoramas(path[i][1], path[i][0])

        # print(pan_id)
        # continue
        if pan_id == [] or not pan_id:
            continue
        pan_view = get_panorama(pan_id[-1].pano_id)
        pan_view.save(f'image{i}.jpg', 'jpeg')


if __name__ == "__main__":
    walk("Самарский политехнический университет", "Самарский университет Королева")
