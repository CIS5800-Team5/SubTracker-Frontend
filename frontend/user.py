ctx = {
       'user' : request.user
      }

if request.user.is_authenticated():
    ctx.update({
         'first_name': request.user.first_name,
         'last_name': request.user.last_name,
         'email' : request.user.email
    })
