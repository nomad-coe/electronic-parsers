import matplotlib.pyplot as plt
from ase.visualize.plot import plot_atoms
from ase.lattice.cubic import FaceCenteredCubic
from ase.io import read, write
from ase import Atoms
from ase.geometry.analysis import Analysis
from ase.visualize import view

slab = read("geometry.in.next_step.in")

z_cut=24
vacuum_cut=50

#slab.symbols[0]="Ge"
#slab.symbols[1]="Ge"

required_positions=[[[slab.get_positions()[i][0],slab.get_positions()[i][1],slab.get_positions()[i][2]-z_cut],slab.symbols[i]] for i in range(len(slab.get_positions())) if slab.get_positions()[i][2]> z_cut]
new_cell=[slab.get_cell()[0],slab.get_cell()[1],[0,0,slab.get_cell()[2][2]-vacuum_cut]]

new_slab=Atoms([i[1] for i in required_positions],cell=new_cell,positions=[i[0] for i in required_positions])
ana = Analysis(new_slab)
bonds= ana.unique_bonds


offset_x=0.77
offset_y=0.28
offset_z=0.58
def bonds_plot(Atoms,each_atom_list,index,subfig,n):
    list_of_bonds=[]
    center_atom=Atoms.get_positions()[index]
    #print(center_atom)
    for i in each_atom_list:
        bonded_atom=Atoms.get_positions()[i]
        #print(bonded_atom)
        x_list=[center_atom[0]+offset_x,bonded_atom[0]+offset_x]
        y_list=[center_atom[1]+offset_y,bonded_atom[1]+offset_y]
        z_list=[center_atom[2]+offset_z,bonded_atom[2]+offset_z]
        if n==0:
            subfig.plot(x_list,y_list,"k-")
        elif n==1:
            subfig.plot(x_list,z_list,"k-")
        elif n==2:
            subfig.plot(y_list,z_list,"k-")

def change_color_adatom(symbol1,symbol2):
    if symbol1=="Ga" and symbol2=="Ga":
        new_slab.symbols[0]="Ge"
        new_slab.symbols[1]="Ge"
    if symbol1=="Ga" and symbol2=="O":
        new_slab.symbols[0]="Ge"
        new_slab.symbols[1]="N"
    if symbol1=="O" and symbol2=="Ga":
        new_slab.symbols[0]="N"
        new_slab.symbols[1]="Ge"
    if symbol1=="O" and symbol2=="O":
        new_slab.symbols[0]="N"
        new_slab.symbols[1]="N"    

change_color_adatom(new_slab.symbols[0],new_slab.symbols[1])
fig, axarr = plt.subplots(1, 3, figsize=(15, 5))
positions=[item[0] for item in required_positions]
symbols=[item[1] for item in required_positions]

#for i in range(len(positions)):   
#    if symbols[i]=="Ga":
#       color_style="bo" 
#       size=27
#    if symbols[i]=="O":
#       color_style="ro"
#       size=14
#    if symbols[i]=="Ge":
#       color_style="go"
#       size=27
#    if symbols[i]=="N":
#       color_style="mo"
#       size=14
#    axarr[0].plot(positions[i][0],positions[i][1],color_style,markersize=size)
#    axarr[1].plot(positions[i][0],positions[i][2],color_style,markersize=size)
#    axarr[2].plot(positions[i][1],positions[i][2],color_style,markersize=size)

plot_atoms(new_slab, axarr[0], radii=0.5,scale=1.0, offset=(0, 0),rotation=('0x,0y,0z'),show_unit_cell=0)

for i in range(len(bonds[0])):
    bonds_plot(new_slab,bonds[0][i],i,axarr[1],1)

plot_atoms(new_slab, axarr[1], radii=0.5, scale=1.0, offset=(0, 0), rotation=('-90x,0y,0z'))

for i in range(len(bonds[0])):
    bonds_plot(new_slab,bonds[0][i],i,axarr[2],2)

plot_atoms(new_slab, axarr[2], radii=0.5, scale=1.0, offset=(0, 0), rotation=('-90x,-90y,0z'))


axarr[0].set_xlabel("a [$\mathrm{\AA}$]")
axarr[0].set_ylabel("b [$\mathrm{\AA}$]")
axarr[1].set_xlabel("a [$\mathrm{\AA}$]")
axarr[1].set_ylabel("c [$\mathrm{\AA}$]")
axarr[2].set_xlabel("b [$\mathrm{\AA}$]")
axarr[2].set_ylabel("c [$\mathrm{\AA}$]")
#axarr[3].set_xlim(2, 6)
#axarr[3].set_ylim(2, 6)
#axarr[0].set_xlim(-1,10.14)
#axarr[0].set_ylim(-1,12.62)
#axarr[0].figsize=(20, 8)
#axarr[1].set_xlim(-1,10.14)
#axarr[1].set_ylim(-1,24)
#axarr[2].set_xlim(-1,12.62)
#axarr[2].set_ylim(-1,24)
#fig.subplots_adjust(wspace=-0.3, hspace=-0.3)
plt.subplots_adjust(left=0.1,
                    right=0.75, 
                    wspace=0, 
                    hspace=0)
#fig.tight_layout()
#plt.show()
fig.savefig("ase_slab_multiple.pdf")
