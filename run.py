from taskbox import app, config

if __name__ == "__main__":
    app.run(debug=True)
                # Resets table on app start;
    #config.resetDB()   # comment this out if you don't want that to happen 