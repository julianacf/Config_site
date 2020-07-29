from django.shortcuts import render

# Create your views here.
def config(request):
    return render(request, 'config_site/config.html', {})

def op_mode_select(request):
    form = ConfigForm()
    return render(request, 'config_site/config.html', {'form': form})
