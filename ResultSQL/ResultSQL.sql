SELECT c.name, COUNT(DISTINCT cc.comic_id) AS comic_count
FROM character_comics AS cc
INNER JOIN characters AS c ON c.id = cc.character_id
GROUP BY c.name;

#-------------------------------------------------------------------
#character_name ||| comic_count
#------------------------------------------------------------------
#!Don't run this script as is