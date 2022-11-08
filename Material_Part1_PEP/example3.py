def validate_data_dict(data_dict):
    """ put explanation here
    """
    if not data_dict:
        raise ValueError("data_dict is empty")
        
    for item_one, item_two in data_dict.items():
    
        if not item_two:
            raise ValueError(f"The dict content under {item_one} is empty.")
            
        if not isinstance(item_two, dict):
            raise ValueError(
                f"The content of {item_one} is not a dict but {type(item_two)}."
            )

        list_ = ["data", "file_type", "sofa", "paragraph"]
        missing_cats = []
        for category in list_:
            if category not in list(item_two.keys()):
                missing_cats.append(category)

        if missing_cats:
            raise ValueError(f"Data dict is missing categories: {missing_cats}")


if __name__ == "__main__":
    data_dict = {}
    data_dict = {"test": {"testing": "just testing"}}
    validate_data_dict(data_dict)