from django.shortcuts import render, redirect, get_object_or_404, reverse





class ObjectUpdateMixin:
    bound_form = None
    template = None
    obj_class = None

    def get(self, request, id):
        obj = get_object_or_404(self.obj_class, id=id)
        bound_form = self.bound_form(instance=obj)
        return render(request, self.template, context={'form': bound_form,
                                                       self.obj_class.__name__.lower(): obj})

    def post(self, request, id):
        obj = get_object_or_404(self.obj_class, id=id)
        bound_form = self.bound_form(request.POST, instance=obj)
        if bound_form.is_valid():
            obj = bound_form.save()
            return redirect(obj)
        return render(request, self.template, context={'form': bound_form, self.obj_class.__name__.lower(): obj})


class ObjectDeleteMixin:
    template = None
    obj_class = None
    redirect_template = None

    def get(self, request, id):
        obj = get_object_or_404(self.obj_class, id=id)
        return render(request, self.template, context={self.obj_class.__name__.lower(): obj})

    def post(self, request, id):
        obj = get_object_or_404(self.obj_class, id=id)
        obj.delete()
        return redirect(reverse(self.redirect_template))