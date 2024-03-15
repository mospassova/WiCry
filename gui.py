from flask import Flask, request, render_template_string
import subprocess

app = Flask(__name__)

HTML = '''
<!doctype html>
<html>
<head>
<title>SSID Command Runner</title>
</head>
<body>
  <h2>SSID Command Runner</h2>
  <form method="post">
    SSID: <input type="text" name="ssid"><br>
    <input type="submit" name="action" value="Learn">
    <input type="submit" name="action" value="Active">
  </form>
</body>
</html>
'''

@app.route('/', methods=['GET', 'POST'])
def ssid_command():
    if request.method == 'POST':
        ssid = request.form['ssid']
        action = request.form['action']
        
        if action == 'Learn':
            command = f"./RAPD -learning \"{ssid}\""
        elif action == 'Active':
            command = f"./RAPD -active \"{ssid}\""
        else:
            return "Invalid action", 400

        try:
            subprocess.run(command, shell=True, check=True)
            return f"Command executed successfully: {command}"
        except subprocess.CalledProcessError as e:
            return f"Error executing command: {e}", 500

    return render_template_string(HTML)

if __name__ == '__main__':
    app.run(debug=True)
