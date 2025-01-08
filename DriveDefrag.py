import os
import ctypes
import subprocess
import platform

class DriveDefrag:
    def __init__(self, drive_letter='C'):
        self.drive_letter = drive_letter.upper()

    def check_platform(self):
        if platform.system() != "Windows":
            raise EnvironmentError("DriveDefrag is only supported on Windows platforms.")

    def is_admin(self):
        try:
            return ctypes.windll.shell32.IsUserAnAdmin()
        except:
            return False

    def defragment_drive(self):
        print(f"Starting defragmentation of drive {self.drive_letter}:")
        try:
            subprocess.run(['defrag', f'{self.drive_letter}:', '/O'], check=True)
            print(f"Defragmentation of drive {self.drive_letter}: completed successfully.")
        except subprocess.CalledProcessError as e:
            print(f"An error occurred while defragmenting the drive: {e}")

    def optimize_drive(self):
        print(f"Starting optimization of drive {self.drive_letter}:")
        try:
            subprocess.run(['defrag', f'{self.drive_letter}:', '/X'], check=True)
            print(f"Optimization of drive {self.drive_letter}: completed successfully.")
        except subprocess.CalledProcessError as e:
            print(f"An error occurred while optimizing the drive: {e}")

def main():
    drive_letter = input("Enter the drive letter to defragment and optimize (e.g., C): ")
    defragger = DriveDefrag(drive_letter)
    
    defragger.check_platform()

    if not defragger.is_admin():
        print("Administrator privileges are required to defragment and optimize drives.")
        return

    defragger.defragment_drive()
    defragger.optimize_drive()

if __name__ == "__main__":
    main()