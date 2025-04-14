def register_routes(app):
    from .slash_route import slash_blueprint;
    from .representative.representative_create_route import create_representant_blueprint;
    from .representative.representative_delete_route import delete_representative_blueprint

    # slash
    app.register_blueprint(slash_blueprint);

    # representant
    app.register_blueprint(create_representant_blueprint)
    app.register_blueprint(delete_representative_blueprint)

    # enterprise

    # client

    # product