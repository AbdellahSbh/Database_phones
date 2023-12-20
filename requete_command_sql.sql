/*Interview:
Table des téléphones :
Cette table stocke les détails des différents modèles de téléphones disponibles. Pour chaque téléphone, elle comprend des informations telles que la marque, le modèle, l'année de sortie, le système d'exploitation, les spécifications techniques comme la taille de l'écran, le type de processeur, la mémoire RAM, la capacité de stockage, la résolution de la caméra, la capacité de la batterie et le prix.

Table des clients :
Cette table contient des informations sur les clients qui achètent des téléphones. Elle inclut des détails tels que le nom du client, sa localisation, son adresse e-mail et son numéro de téléphone.

Table des achats :
Cette table enregistre les détails des achats effectués par les clients. Chaque enregistrement lie un client à un téléphone spécifique et inclut la date de l'achat ainsi que la quantité achetée.

Table des stocks :
Cette table est utilisée pour suivre le stock des différents modèles de téléphones. Elle indique combien d'unités de chaque modèle de téléphone sont disponibles en stock.

Table des magasins :
Cette table fournit des informations sur les magasins où les téléphones sont vendus. Pour chaque magasin, elle stocke le nom et la localisation.

En résumé, cette base de données permet de gérer efficacement les informations sur les téléphones disponibles, les clients qui les achètent, les transactions d'achat, le suivi des stocks et les magasins qui vendent ces téléphones. Les relations entre ces tables aident à organiser et à analyser les données de manière cohérente et efficace.*/
-- Création de la table des clients
CREATE TABLE clients (
    id_client INTEGER PRIMARY KEY AUTOINCREMENT, -- Identifiant unique pour chaque client
    nom TEXT, -- Nom du client
    localisation TEXT, -- Localisation géographique du client
    email TEXT UNIQUE, -- Adresse e-mail du client, doit être unique
    numero_telephone TEXT -- Numéro de téléphone du client
);

-- Création de la table des achats
CREATE TABLE achats (
    id_achat INTEGER PRIMARY KEY AUTOINCREMENT, -- Identifiant unique pour chaque achat
    id_client INTEGER, -- Identifiant du client qui a effectué l'achat
    id_telephone INTEGER, -- Identifiant du téléphone acheté
    date_achat DATE, -- Date de l'achat
    quantite INTEGER, -- Quantité de téléphones achetés
    FOREIGN KEY (id_client) REFERENCES clients(id_client), -- Clé étrangère reliant à la table des clients
    FOREIGN KEY (id_telephone) REFERENCES telephones(id_telephone) -- Clé étrangère reliant à la table des téléphones
);

-- Création de la table des stocks
CREATE TABLE stocks (
    id_stock INTEGER PRIMARY KEY AUTOINCREMENT, -- Identifiant unique pour chaque entrée de stock
    id_telephone INTEGER, -- Identifiant du téléphone en stock
    quantite_en_stock INTEGER, -- Quantité de ce téléphone disponible en stock
    FOREIGN KEY (id_telephone) REFERENCES telephones(id_telephone) -- Clé étrangère reliant à la table des téléphones
);

-- Création de la table des magasins
CREATE TABLE magasins (
    id_magasin INTEGER PRIMARY KEY AUTOINCREMENT, -- Identifiant unique pour chaque magasin
    nom_magasin TEXT, -- Nom du magasin
    localisation TEXT -- Localisation géographique du magasin
);
