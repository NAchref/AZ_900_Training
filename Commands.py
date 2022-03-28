#Creating Resource Group(to hold all the things thats we need)
az group create --name --location

#Install IIS(Internet Information Services)
dism  \online  \enable-feature  \featurename:IIS-webServerRole

#Open port Command : 
az Vm open-port
 
#Open port 80 HTTP : 
az Vm open-port
--name myVm
--resource-group Learn-47dn3r45nke
--port 80
