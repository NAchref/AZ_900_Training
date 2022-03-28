#Creating Resource Group(to hold all the things thats we need)
az group create --name --location

#Install IIS(Internet Information Services)
dism  \online  \enable-feature  \featurename:IIS-webServerRole

#Open port Command : 
az Vm open-port
 
#Open port 80 HTTP : 
az Vm open-port \
--name myVm \
--resource-group Learn-ed49b49c-4d23-418b-89c2-7d6186579226 \
--port 80 \

#Verify Vm's running and show command list public IP adresse
az vm show \
 --name myVM \
 --resource-group Learn-ed49b49c-4d23-418b-89c2-7d6186579226 \
 --show-details \
 --query [publicIps] \
 --output tsv
