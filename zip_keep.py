# zip the kept folder if needed

import shutil
shutil.make_archive("kept_photos", 'zip', "keep")
print("done")