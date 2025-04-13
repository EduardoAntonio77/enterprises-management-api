def register_routes(app):
    from .slash_route import slash_blueprint;
    from .representative_create_route import create_representant_blueprint;

    # slash
    app.register_blueprint(slash_blueprint);

    # representant
    app.register_blueprint(create_representant_blueprint)

    # enterprise

    # client

    # product