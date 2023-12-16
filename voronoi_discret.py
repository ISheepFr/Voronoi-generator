import random
import argparse

import cv2
import numpy as np


def distanceEuclidienne(p1,p2):
    return np.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

def distanceAbs(p1,p2):
    return (np.abs(p1[0]-p2[0]) + np.abs(p1[1]-p2[1]))

def distanceInf(p1,p2):
    return max(np.abs(p1[0]-p2[0]),np.abs(p1[1]-p2[1]))

def main():
    parser = argparse.ArgumentParser(description='voronoi_discret')
    parser.add_argument('nb_germes', type=int, default=10,help='Nombre de germes')
    parser.add_argument('--dist', type=int, default=0, help='0 (euclidien) / 1(abs) / 2(infini)')
    parser.add_argument('--img',help='image path')


    args = parser.parse_args()

    #nb germes, path de l'image, fonction de distance renseigné par l'utilisateur
    nbgermes = args.nb_germes
    img_path = args.img

    if args.dist == 0:
        dist_function = distanceEuclidienne
    elif args.dist == 1:
        dist_function = distanceAbs
    elif args.dist == 2:
        dist_function = distanceInf


    if img_path is not None:
        #img_no_resize = cv2.imread(img_path)
        #img = cv2.resize(img_no_resize, None, fx=0.5,fy=0.5)
        img = cv2.imread(img_path)
        img_to_modif = img.copy()
    else:
        img = np.zeros((300,300, 3), np.uint8)
        img_to_modif = img.copy()

    width, height, _ = img.shape

    #va contenir les couleurs des pixels
    ensemble_pixel_couleur = []
    #va contenir les pixels
    ensemble_pixel = []

    #Initialise les pixels:
    #pixel random compris dans l'image
    #couleurs de pixel random si pas d'image sinon sa couleur
    for i in range(0,nbgermes):
        pixel = [random.uniform(0,width-1).__round__(),random.uniform(0,height-1).__round__()]
        couleur_pixel = [random.uniform(0,255).__round__(),random.uniform(0,255).__round__(),random.uniform(0,255).__round__()]
        ensemble_pixel.append(pixel)
        if img_path is not None:
            ensemble_pixel_couleur.append(img[pixel[0],pixel[1]])
        else:
            ensemble_pixel_couleur.append(couleur_pixel)

    #stocke le diagramme de voronoi
    diagramme_voronoi =[]

    #Parcours de l'image
    for x in range (0,width ):
        for y in range (0,height ):
            dist = []

            #calcule et stocke la distance du pixel courant au ensemble de pixel
            for pix in ensemble_pixel:
                dist.append(dist_function((x,y),pix))

            #stocke l'index du pixel dans l'ensemble le + proche du pixel courant
            min_dist = dist.index(min(dist))
            diagramme_voronoi.append(min_dist)

            #affecte la couleur du pixel courant a la couleur du pixel présent dans l'ensemble
            img_to_modif[x,y] = ensemble_pixel_couleur[min_dist]

    if img_path is not None:
        
        # Pour toutes les germes
        for i in range(nbgermes):
            # Indice des pixels qui appartiennent à la germe
            indices = np.where(diagramme_voronoi == i)
            moyenne = np.array([0, 0, 0], dtype=np.float64)

            # Calcule la moyenne de la zone/germe actuelle
            for j in range(1, len(indices[0])):
                pix = (indices[0][j], indices[1][j])
                moyenne += img_to_modif[pix[0], pix[1]]

            moyenne /= (len(indices[0]) - 1)

            # Application des couleurs avec la moyenne
            for j in range(1, len(indices[0])):
                pixel_2_color = (indices[0][j], indices[1][j])
                img_to_modif[pixel_2_color[0], pixel_2_color[1]] = moyenne




    if img_path is None:
        for pixel in ensemble_pixel:
            cv2.circle(img_to_modif,(pixel[1],pixel[0]),5,(0,0,255))

    cv2.imshow("Original",img)
    cv2.imshow("Voronoi",img_to_modif)
    cv2.imwrite('end.jpg',img_to_modif)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()