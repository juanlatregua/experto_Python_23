from django.shortcuts import render
from review.models import Review, Comment
from review.forms import CommentForm

# Create your views here.

def review_index(request):
    reviews = Review.objects.all().order_by('-created_on')
    context = {
        "reviews": reviews,
    }
    return render(request, "review_index.html", context)

def review_category(request, category):
    reviews = Review.objects.filter(categories__name__contains=category).order_by('-created_on')
    context = {
        "category": category,
        "reviews": reviews
    }
    return render(request, "review_category.html", context)

def review_detail(request, pk):
    review = Review.objects.get(pk=pk)

    form = CommentForm()
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = Comment(
                author=form.cleaned_data["author"],
                body=form.cleaned_data["body"],
                review=review
            )
            comment.save()

    comments = Comment.objects.filter(review=review)
    context = {
        "review": review,
        "comments": comments,
        "form": form,
    }

    return render(request, "review_detail.html", context)