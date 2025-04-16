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

    # product