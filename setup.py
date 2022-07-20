import cx_Freeze

executables = [cx_Freeze.Executable('main.py')]

cx_Freeze.setup(
  name= 'Jogo da Velha',
  options={'build_exe':{'packages':['pygame'],
                          'include_files':['scripts','sounds','img']}},
  executables=executables
)