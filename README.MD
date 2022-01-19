**NFT-Generator** is the best way to generate thousands of NFTs quick and easily with Python. Just add your files, set your configuration and run the script. You'll get all the images and metadata required for your NFT project!

## How to use?
1. Clone the repo by running `git clone https://github.com/itshydrone/NFT-Generator.git`
2. Enter the downloaded directory by typing `cd NFT-Generator`
3. Install the dependencies by running `pip install -r requirements.txt`
4. Add all your layer files in the 'traits' folder. They should be separated in different layer folders.
5. Add the probability of each trait. You can do this by adding the number after a '#' in the file name. For example, if the 'Background' layer had two files called 'Black#50.png' and 'White#50.png' then there would be a 50% chance of each being selected.
6. Edit the `config.py` file with your settings.
7. Run `generator.py`

## Traits Setup
traits/
├─ layer1_name/
│ ├─ file1#10.png
│ ├─ file2#10.png
│ ├─ file3#80.png
│ ├─ ...
├─ layer2_name/
│ ├─ file1#50.png
│ ├─ file2#50.png
│ ├─ ...
├─ layer3_name/
│ ├─ file1#100.png
│ ├─ ...

## Image file Setup
file1#100.png => `[file_name]`#`[rarity_value]`.png