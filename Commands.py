#Creating Resource Group(to hold all the things thats we need)
az group create --name --location

#Create a VM1 in resource group RG1 with image Ubuntu
az vm create --resource-group RG1 --name VM1 --image UbuntuLTS 
--generate-ssh-keys

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

#Increase your VM’s size to Standard_DS3_v2
az vm resize \
 --resource-group Learn-ed49b49c-4d23-418b-89c2-7d6186579226 \
 --name myVM \
 --size Standard_DS3_v2

#Verify that your VM is running the new size
az vm show \
 --resource-group Learn-ed49b49c-4d23-418b-89c2-7d6186579226 \
 --name myVM \
 --query "hardwareProfile" \
 --output tsv

#Delete a virtual machine named 'MyVm'. 
az resource delete -g MyResourceGroup -n MyVm --resource-type "Microsoft.Compute/virtualMachines"

#Power-off a vm, specified by Id
az resource invoke-action --action powerOff \
  --ids /subscriptions/{SubID}/resourceGroups/{ResourceGroup}/providers/Microsoft.Compute/virtualMachines/{VMName}

#Delete a web app using a resource identifier
az resource delete --ids /subscriptions/0b1f6471-1bf0-4dda-aec3-111111111111/resourceGroups/MyResourceGroup/providers/Microsoft.Web/sites/MyWebapp
