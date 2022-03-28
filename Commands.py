#install IIS(Internet Information Services)
dism  \online  \enable-feature  \featurename:IIS-webServerRole


#open port Command : 
  az Vm open-port
 
#open port 80 HTTP : 
az Vm open-port
--name myVm
--resource-group Learn-47dn3r45nke
--port 80
