def register_routes(app):
    # slash_route
    from .slash_route import slash_blueprint;
    
    # representative_route
    from .representative.representative_create_route import create_representant_blueprint;
    from .representative.representative_delete_route import delete_representative_blueprint;
    from .representative.representative_edit_route import edit_representative_blueprint;
    
    # Enterprise_route
    from .enterprise.enterprise_create_route import create_enterprise_blueprint;
    from .enterprise.enterprise_edit_route import enterprise_edit_blueprint;
    from .enterprise.enterprise_delete_route import enterprise_delete_blueprint

    # Client_route
    from .client.client_create_route import client_create_blueprint
    from .client.client_delete_route import client_delete_blueprint
    from .client.client_edit_route import client_edit_blueprint

    # Product_route
    from .product.product_create_route import product_create_blueprint
    from .product.product_delete_route import product_delete_blueprint
    from .product.product_edit_route import product_edit_blueprint


    # slash
    app.register_blueprint(slash_blueprint);

    # representant
    app.register_blueprint(create_representant_blueprint);
    app.register_blueprint(delete_representative_blueprint);
    app.register_blueprint(edit_representative_blueprint);
    

    # enterprise
    app.register_blueprint(create_enterprise_blueprint);
    app.register_blueprint(enterprise_edit_blueprint);
    app.register_blueprint(enterprise_delete_blueprint);
    

    # client
    app.register_blueprint(client_create_blueprint)
    app.register_blueprint(client_delete_blueprint)
    app.register_blueprint(client_edit_blueprint)

    # product
    app.register_blueprint(product_create_blueprint)
    app.register_blueprint(product_delete_blueprint)
    app.register_blueprint(product_edit_blueprint)