import yaml
import yamldown

md_str = ''
result = None
with open("recipes.yml") as f_in:
    recipes = yaml.load(f_in, Loader=yaml.FullLoader)
    result = yamldown.dump(recipes, md_str)
     

    for recipe, recipe_info in recipes.items():
        print(recipe)
        for k, v in recipe_info.items():
            print(f"\t{k}: {v}")
    
print("md str")
with open("recipes.md","w") as f_out:
    f_out.write(result)
print(result)
