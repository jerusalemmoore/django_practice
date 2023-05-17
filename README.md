# django_practice
playing around with django while learning more about web programming fundamentals(Bootstrap/JS), deployed using docker
  As this is running on docker i believe this should currently be deployable as long as docker daemon is installed and running, at least on Windows
  will need to test, but as long as this is the case. project should be runnable via powershell
  for windows:  
    1. docker-compose build   
    2. docker-compose up  
    3. access through: http://localhost:8000/blog/
   
  
    note: still need to take care of possible race conditions in service start:).
    web service in docker-compose.yml may start before livereload does but this 
    shouldn't be  an issue if you're just looking around. the web service may start  
    before the db is up and running on first time run   
    but usually comes up fine on the second run of the build.
    note: for linux, you may need to prepend the above commands with "sudo" 
    
