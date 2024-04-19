from flask import Flask, request, render_template_string, redirect, url_for
import subprocess

app = Flask(__name__)

HTML = '''
<!doctype html>
<script>
  function showAlert() {
    alert("The output of the program is in the console.");
  }
</script>
<html>
<head>
<title>SSID Command Runner</title>
</head>
<body>
  <h2>RAPD by zaLOOPenite</h2>
  <form method="post">
    SSID: <input type="text" name="ssid"><br>
    <input type="submit" name="action" value="Learn">
    <input type="submit" name="action" value="Active" onclick="showAlert()">
    <input type="submit" name="action" value="known.txt"><br><br>
    <textarea rows="1" cols="50" readonly>The RogueAP/Evil Twin candidates are shown in the console</textarea>
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
        elif action == 'known.txt':
            return redirect(url_for('view_known_file'))  # Redirect to view known.txt
        else:
            return "Invalid action", 400

        try:
            subprocess.run(command, shell=True, check=True)
            return f"Command executed successfully: {command}"
        except subprocess.CalledProcessError as e:
            return f"Error executing command: {e}", 500

    return render_template_string(HTML)

@app.route('/known.txt', methods=['GET', 'POST'])
def view_known_file():
    if request.method == 'GET':
        # Read the content of known.txt file
        with open('known.txt', 'r') as file:
            content = file.read()
        return content

    elif request.method == 'POST':
        # Update the content of known.txt file
        new_content = request.form['content']
        with open('known.txt', 'w') as file:
            file.write(new_content)
        return "File updated successfully"

if __name__ == '__main__':
    app.run(debug=True)
