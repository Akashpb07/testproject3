from django.db.models import Count, Q
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.views.generic import View, ListView, DetailView, CreateView, UpdateView, DeleteView


from .models import Stories, StoriesView , contact_us_detail
from .forms import ContactForm ,AddStoryForm
from marketing.forms import EmailSignupForm
from marketing.models import Signup
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User, auth
from django.views import generic
from django.contrib.messages.views import SuccessMessageMixin
form = EmailSignupForm()

def features(request):
    feature = features.objects.all()
    context = {
        'feature': feature,
    }
    return render(request, 'index.html', context)

def view_profile(request, pk=None):
    if pk:
        user = User.objects.get(pk=pk)
    else:
        user = request.user
    args = {'user': user}
    return render(request, 'profile.html', args)

class contactUs(SuccessMessageMixin, generic.CreateView):
    form_class = ContactForm
    template_name = "contactus1.html"
    success_url = "/contact_us"
    success_message = "Your query has been submited successfully, we will contact you soon."

    def form_invalid(self, form):
        messages.add_message(self.request, messages.ERROR, "Please submit the form carefully. You missed some fields")
        return redirect('contact_us')



class StorySearchView(View):
    def get(self, request, *args, **kwargs):
        queryset1 = Stories.objects.all()
        query = request.GET.get('q')
        if query:
            queryset1 = queryset1.filter(
                Q(title__icontains=query) |
                Q(overview__icontains=query)
            ).distinct()
        context = {
            'queryset1': queryset1
        }
        return render(request, 'story_search_results.html', context)


def searchstory(request):
    queryset1 = Stories.objects.all()
    query = request.GET.get('q')
    if query:
        queryset1 = queryset1.filter(
            Q(student_name__icontains=query) |
            Q(student_overview__icontains=query)
        ).distinct()
    context = {
        'queryset1': queryset1
    }
    return render(request, 'story_search_results.html', context)


def get_category_count():
    queryset = Stories \
        .objects \
        .values('categories__title') \
        .annotate(Count('categories__title'))
    return queryset


class IndexStorieView(View):
    form = EmailSignupForm()


    def get(self, request, *args, **kwargs):
        featured = Stories.objects.filter(featured=True)
        latest_stories = Stories.objects.order_by('-timestamp')[0:3]
        context = {
            'object_list': featured,
            'latest_stories': latest_stories,
            'form': self.form
        }
        return render(request, 'index.html', context)

    def post(self, request, *args, **kwargs):
        email = request.POST.get("email")
        new_signup = Signup()
        new_signup.email = email
        new_signup.save()
        messages.info(request, "Successfully subscribed")
        return redirect("home")


def index_1(request):
    featured = Stories.objects.filter(featured=True)
    latest_stories = Stories.objects.order_by('-timestamp')[0:3]

    if request.method == "POST":
        email = request.POST["email"]
        new_signup = Signup()
        new_signup.email = email
        new_signup.save()

    context = {
        'object_list': featured,
        'latest_stories': latest_stories,
        'form': form
    }
    return render(request, 'index.html', context)

class StoryListView(ListView):
    form = EmailSignupForm()
    model = Stories
    template_name = 'stories.html'
    context_object_name = 'queryset'
    paginate_by = 1

    def get_context_data(self, **kwargs):
        category_count = get_category_count()
        most_recent = Stories.objects.order_by('-timestamp')[:3]
        context = super().get_context_data(**kwargs)
        context['most_recent'] = most_recent
        context['page_request_var'] = "page"
        context['category_count'] = category_count
        context['form'] = self.form
        return context


def story_list(request):

    most_recent = Stories.objects.order_by('-timestamp')[:3]
    story_list = Stories.objects.order_by('-timestamp')
    paginator = Paginator(story_list, 4)
    page_request_var = 'page'
    page = request.GET.get(page_request_var)
    try:
        paginated_queryset = paginator.page(page)
    except PageNotAnInteger:
        paginated_queryset = paginator.page(1)
    except EmptyPage:
        paginated_queryset = paginator.page(paginator.num_pages)

    context = {
        'queryset': paginated_queryset,
        'page_request_var': page_request_var,
        'most_recent': most_recent,
        'form': form
    }
    return render(request, 'story_t1.html', context)


class StoryDetailView(DetailView):
    model = Stories
    template_name = 'story_deatils.html'
    context_object_name = 'story'


    # def get_object(self):
    #     # obj = super().get_object()
    #     # # if self.request.user.is_authenticated:
    #     # #     Stories.objects.get_or_create(
    #     # #         user=self.request.user,
    #     # #         post=obj
    #     # #     )
    #     # # return obj

    def get_context_data(self, **kwargs):

        most_recent = Stories.objects.order_by('-timestamp')[:3]
        context = super().get_context_data(**kwargs)
        context['most_recent'] = most_recent
        context['page_request_var'] = "page"

        # context['form'] = self.form
        return context

    def story(self, request, *args, **kwargs):

        if form.is_valid():
            Stories = self.get_object()
            form.instance.user = request.user
            form.instance.story = Stories
            form.save()
            return redirect(reverse("story-detail", kwargs={
                'pk': Stories.pk
            }))


def story_detail(request, id):
    category_count = get_category_count()
    most_recent = Stories.objects.order_by('-timestamp')[:3]
    post = get_object_or_404(Stories, id=id)

    if request.user.is_authenticated:
        StoriesView.objects.get_or_create(user=request.user, post=post)


    if request.method == "POST":
        if form.is_valid():
            form.instance.user = request.user
            form.instance.story = Stories
            form.save()
            return redirect(reverse("story-detail", kwargs={
                'id': Stories.pk
            }))
    context = {
        'Stories': Stories,
        'most_recent': most_recent,
        'category_count': category_count,
        'form': form
    }
    return render(request, 'story_deatils.html', context)


class StoryCreateView(CreateView , SuccessMessageMixin):
    model = Stories
    template_name = 'story_create.html'
    success_message = "Story has been addded successfully"
    form_class = AddStoryForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Add'
        return context

    def form_valid(self, form):

        form.save()
        return redirect(reverse("story-detail", kwargs={
            'pk': form.instance.pk
        }))


def story_create(request):
    title = 'Add Story'
    form = AddStoryForm(request.POST or None, request.FILES or None)

    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect(reverse("story-detail", kwargs={
                'id': form.instance.id
            }))
    context = {
        'title': title,
        'form': form
    }
    return render(request, "story_create.html", context)

class StoryDeleteView(DeleteView,SuccessMessageMixin):
    model = Stories
    success_url = '/story'
    success_message = "Story has been deleted successfully!"
    template_name = 'story_confirm_delete.html'


def story_delete(request, id):
    story = get_object_or_404(Stories, id=id)
    story.delete()
    return redirect(reverse("Story-list"))


class StoryUpdateView(UpdateView):

    success_message = "Story has been updated successfully!"
    model = Stories
    template_name = 'story_create.html'
    form_class = AddStoryForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Update'
        return context

    def form_valid(self, form):

        form.save()
        return redirect(reverse("story-detail", kwargs={
            'pk': form.instance.pk
        }))


def story_update(request, id):
    title = 'Update story'
    post = get_object_or_404(Stories, id=id)
    form = AddStoryForm(
        request.POST or None,
        request.FILES or None,
        instance=post)

    if request.method == "POST":
        if form.is_valid():

            form.save()
            return redirect(reverse("story-detail", kwargs={
                'id': form.instance.id
            }))
    context = {
        'title': title,
        'form': form
    }
    return render(request, "story_create.html", context)


