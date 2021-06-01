# FancyNodeGraph

FancyNodeGraph is a Katana Tab which extend current katana Node View with external drag and drop Features.

## Installation

 
clone this repo
```bash
git@github.com:achayan/fancy_nodeview.git
```

## Usage

```python
You need to make sure you add your path to KATANA_RESOURCES
example 
setenv KATANA_RESOURCES ~/dev/katana_dev/fancy_nodeview
# windows
set KATANA_RESOURCES=C:\dev\katana_dev\fancy_nodeview
```
One you added `KATANA_RESOURCES` properly then on the `Tabs`Menu you will have `Fancy Node Graph`

Once you have the `Fancy Node Graph` open you will be able to drag and drop files and that will create nodes inside katana.

If you have a node selected then new nodes will be placed under that or at 0 0 

You can extend file types in line 10
```python
# you need to give file extension type and node type and attribute name
".abc":["Alembic_In", "abcAsset"], ".usd":["UsdIn", "fileName"],".usda":["UsdIn", "fileName"],".usdc":["UsdIn", "fileName"], ".usdz":["UsdIn", "fileName"]}
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)