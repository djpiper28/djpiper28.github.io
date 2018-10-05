import os
import subprocess

ad = "\n<iframe id=\"ad\" class='iframe' data-aa='535860' src='//ad.a-ads.com/535860?size=336x280' scrolling='no' style='width:336px; height:280px; border:0px; padding:0;overflow:hidden' allowtransparency='true'></iframe>"
#Folder with the source code in
rootFolder = "C:/Users/djpip/Documents/My Games/Terraria/ModLoader/Mod Sources/PostMoonLord"
rootFolder_ = "C:\\Users\\djpip\\Documents\\My Games\\Terraria\\ModLoader\\Mod Sources\\PostMoonLord"
#Folders with modded content
folders = ["Buffs","Items","Mounts","NPCs","Projectiles","Tiles","Walls","Items/Armour","NPCs/thepossessed","NPCs/mobs","NPCs/Cryptys","Items/croliumgreatblade"]
#Wiki Home Page
homepage = "https://djpiper28.github.io/PostMoonLordWiki/index.html"
Description_tmp = []
Description = ""

f = open((rootFolder+"/description.txt"),"r")

for line in f:
	Description_tmp.append("<p>"+line+"\n</p>\n")

f.close

f = open((rootFolder+"/build.txt"),"r")
for line in f:
	if "version" in line:
		Description_tmp.append("<h3>WIKI VERSION: </h3><p>"+line+"\n</p>\n")

Description = "\n".join(Description_tmp)

style = """
<link href="https://cdn.jsdelivr.net/npm/tailwindcss/dist/tailwind.min.css" rel="stylesheet">
<meta charset="utf-8">
<meta http-equiv="X-UA-Compatible" content="IE=edge">
<meta name="viewport" content="width=device-width, initial-scale=1">
"""

staticTitle = style+"<h1>Terraria: The Desomation of Moon Lord Wiki</h1>\n<p>This was auto generated by a python script made by djpiper28</p>\n<a href=\""+homepage+"\">Wiki homepage</a>\n<p><a href=\"https://djpiper28.github.io/PostMoonLordWiki/PostMoonLord.tmod\">Download the mod</a></p>"

print("Creating download link.")

filetocopy = "C:\\Users\\djpip\\Documents\\My Games\\Terraria\\ModLoader\\Mods\\PostMoonLord.tmod"
copyto = rootFolder_+"\\PostMoonLord.tmod*"

cmd = "xcopy \""+filetocopy+"\" \"C:\\Users\\djpip\\Desktop\\djpiper28.github.io\\djpiper28.github.io\\PostMoonLordWiki\\PostMoonLord.tmod\""

subprocess.call(cmd, shell=True)

items = []
#Get items:
for folder in folders:
	files = os.listdir(rootFolder+"/"+folder)
	ff = folder
	for file in files:
		if ".cs" in file:
			print(file+" was found")
			items.append(file+"|"+ff)

out = []

for item in items:

	print(item+".html Is being created")
	itemFolder = item.split("|")[1]
	itemFile = item.split("|")[0]

	cmd = "echo F| xcopy \""+rootFolder_+"\\"+itemFolder+"\\"+itemFile.split(".")[0]+".png\" \"C:\\Users\\djpip\\Desktop\\djpiper28.github.io\\djpiper28.github.io\\PostMoonLordWiki\\"+itemFile.split(".")[0]+".png*\""

	subprocess.call(cmd, shell=True)
	#print("Copied File "+itemFile.split(".")[0]+".png"+"\nfrom  "+rootFolder+"/"+itemFolder+"/"+itemFile.split(".")[0]+".png  to C:/Users/dp/Desktop/djpiper28.github.io/djpiper28.github.io/PostMoonLordWiki/"+itemFile.split(".")[0]+".png")

	f = open((rootFolder+"/"+itemFolder+"/"+itemFile),"r")
	
	itemDetails = []

	for line in f:
		try: 
			if "DisplayName.SetDefault" in line:
				itemDetails.append("<h3>Name: "+line.split("\"")[1]+"\n</h3>")
                        
			if "Tooltip.SetDefault" in line:
				itemDetails.append("<p>Item Description: "+line.split("\"")[1]+"\n</p>")
                        
			if "item.damage" in line:
				itemDetails.append("<p>Item Damage: "+line.split("=")[1]+"\n</p>")
                        
			if "mod.ProjectileType" in line:
				itemDetails.append("<p>Item Projectile: "+line.split("\"")[1]+"\n</p>")
                        
			if "item.lifeRegen" in line:
				itemDetails.append("<p>Item Life Regen: "+line.split("=")[1]+"\n</p>")
                        
			if "item.useTime" in line:
				itemDetails.append("<p>Item Use Time: "+line.split("=")[1]+"\n</p>")
                
			if "item.knockBack" in line:
				itemDetails.append("<p>Item Knockback: "+line.split("=")[1]+"\n</p>")
                
			if "item.autoReuse" in line:
				itemDetails.append("<p>Item Auto Swing: "+line.split("=")[1]+"\n</p>")
                
			if "item.value" in line:
				itemDetails.append("<p>Item Value: "+line.split("=")[1]+"\n</p>")
                        
			if "item.rare" in line:
				itemDetails.append("<p>Item Rarity: "+line.split("=")[1]+"\n</p>")
                                        
			if "Main.tileSpelunker" in line:
				itemDetails.append("<p>Tile is an Ore: "+line.split("=")[1]+"\n</p>")

			if "npc.damage" in line:
				itemDetails.append("<p>NPC Damage: "+line.split("=")[1]+"\n</p>")

			if "npc.lifeMax" in line:
				itemDetails.append("<p>NPC Life: "+line.split("=")[1]+"\n</p>")

			if "defense" in line:
				try:
					itemDetails.append("<p>Defense: "+line.split("=")[1]+"\n</p>")
				except:
					print(line+"\n\nWas faulty")

			if "npc.boss" in line:
				itemDetails.append("<p>NPC is Boss: "+line.split("=")[1]+"\n</p>")
				
			if "item.pick" in line:
				itemDetails.append("<p>Pickaxe power: "+line.split("=")[1]+"\n</p>")

			if "item.axe" in line:
				itemDetails.append("<p>Axe power: "+line.split("=")[1]+"\n</p>")

			if "item.hammer" in line:
				itemDetails.append("<p>Hammer power: "+line.split("=")[1]+"\n</p>")

			if "recipe.AddIngredient" in line:
				if "null" in line:
					itemDetails.append("<p>Recipe Ingredient: "+line.split(",")[1]+" x "+line.split(",")[2]+"\n</p>")
				else:
					itemDetails.append("<p>Recipe Ingredient: "+line.split("(")[1]+" x "+line.split(",")[1]+"\n</p>")

			if "recipe.AddTile" in line:
				if "null" in line:
					itemDetails.append("<p>Crafted At: "+line.split(",")[1]+"\n</p>")
			else:
					itemDetails.append("<p>Crafted At: "+line.split("(")[1]+"\n</p>")
		except:
			print("something went wrong")
	#<img id="background" src="https://djpiper28.github.io/crChestSim/background.png" alt="background" width="2048" height="1152" class="bg"><img/>
	image = "\n<style>.auto{\nwidth: auto;\nheight: auto;\n}</style>\n<img id=\"image\" src=\"https://djpiper28.github.io/PostMoonLordWiki/"+itemFile.split(".")[0]+".png\" width=\"20%\" height=\"20%\" \"alt=\"Item image\" class=\"auto\"></img>\n"
	out.append("\n<style>.centre{\nmargin: 20%;\n}</style>\n<title>WIKI:"+itemFile.split(".")[0]+"</title>\n<div class='bg-blue text-white text-center py-2 px-2'><div class=\"bg-dark-grey\">"+image+"\n--".join(itemDetails)+"</div>\n"+ad+"</div>")

i = 0

while(i<len(out)):

	d = staticTitle + out[i]

	print(i)

	fileName = items[i].split("|")[0]
	fileName = fileName.split(".")[0]

	f = open(fileName+".html","w+")
	f.close
	f = open(fileName+".html","w")
	f.write(d)
	f.close

	i = i + 1

indexData = []

for item in items:

	fileName = item.split("|")[0]
	fileName = fileName.split(".")[0]

	indexData.append("<p><a href=\"https://djpiper28.github.io/PostMoonLordWiki/"+(fileName+".html")+"\">"+fileName+"</a>\n</p>\n")

print("Creating Index")
f = open("index.html", "w+")
data_To_Write = "<h1>AutoGenerated Wiki Homepage</h1>"+staticTitle+"".join(indexData)+"\n\n\n<p>Copyright djpiper28</p>"
f.write(data_To_Write)
f.close
print("Writing Data")
f = open("index.html", "w")
data_To_Write = "<title>WIKI: Homepage</title><h1>AutoGenerated Wiki Homepage</h1>"+staticTitle+"".join(indexData)+"\n<h3>Description</h4>\n<p>"+Description+"</p>"+ad+"\n\n\n<p>Copyright djpiper28</p>"
f.write(data_To_Write)
f.close
f.close
print(data_To_Write)
print("FINISHED")
