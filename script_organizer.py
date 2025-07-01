from pathlib import Path

class FileOrganizer:
    EXTENCION_DICT = {'.txt': 'Text-Files',
                        '.pdf': 'PDF-Files',
                        '.docx': 'Word-Files',
                        '.jpg': 'Image-Files',
                        '.png': 'Image-Files',
                        '.mp3': 'Audio-Files',
                        '.mp4': 'Video-Files',
                        '.zip': 'Compressed-Files',
                        '.rar': 'Compressed-Files',
                        '.log': 'Log-Files',
                        '.exe': 'Executable-Files',
                        '.jar': 'Java-Files',
                        '.dat': 'Dat-XML-Files',
                        '.xml': 'Dat-XML-Files',
                        '.xlsx': 'Excel-Files'}

    def __init__(self, folder_to_organize:str):
        self.folder_to_organize = Path(folder_to_organize)
        self.generic_folder = "Otros"
    
    def organize_folder(self):
        
        for file in self.folder_to_organize.iterdir():
            if file.is_file():
                if file.suffix.lower() in self.EXTENCION_DICT:
                    move_folder = Path(self.EXTENCION_DICT.get(file.suffix.lower(),self.generic_folder))
                    destination = Path(self.folder_to_organize,move_folder)
                    if destination.exists() and destination.is_dir():
                        file.replace(destination/file.name)
                        print(f"La carpeta {destination} existe. \n -Se movio el archivo {file.name}")
                    else:
                        destination.mkdir()
                        print(f"Se creo la carpeta: {destination}")
                        file.replace(destination/file.name)
                        print(f"{file.name} movido.")


folder_organizer = Path(r"C:\Users\pc250282\Downloads\\")
organizer = FileOrganizer(folder_organizer)
organizer.organize_folder()




