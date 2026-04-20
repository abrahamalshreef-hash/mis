from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.db.models import Q  # لاستخدام البحث المتقدم
from .models import Task
from django.views.decorators.csrf import csrf_exempt


def task_list(request):
    """العرض الرئيسي مع البحث والفلترة وإضافة المهام"""

    # 1. معالجة إضافة مهمة جديدة (POST)
    if request.method == 'POST':
        title = request.POST.get('title', '').strip()
        category = request.POST.get('category', 'personal')
        if title:
            Task.objects.create(title=title, category=category)
        return redirect('task_list')

    # 2. جلب معايير البحث والفلترة من الرابط (GET)
    search_query = request.GET.get('q', '')  # نص البحث
    category_filter = request.GET.get('category', '')  # نوع التصنيف

    # 3. تصفية المهام بناءً على المدخلات
    tasks = Task.objects.all().order_by('-created_at')

    if search_query:
        tasks = tasks.filter(Q(title__icontains=search_query))

    if category_filter:
        tasks = tasks.filter(category=category_filter)

    # 4. جلب التقارير باستخدام المانجر المخصص Task.objects.get_report()
    # (تأكد أن المانجر موجود في models.py كما فعلنا سابقاً)
    report = Task.objects.get_report()

    context = {
        'tasks': tasks,
        'search_query': search_query,
        'category_filter': category_filter,
        **report,  # سيقوم بفك (total, progress, completed_count, remaining_count)
    }
    return render(request, 'tasks/list.html', context)


# باقي الدوال (toggle_task, delete_task, update_duration) تبقى كما هي
def toggle_task(request, pk):
    task = get_object_or_404(Task, id=pk)
    task.completed = not task.completed
    task.save()
    return redirect('task_list')


def delete_task(request, pk):
    get_object_or_404(Task, id=pk).delete()
    return redirect('task_list')


@csrf_exempt
def update_duration(request, task_id):
    if request.method == 'POST':
        task = get_object_or_404(Task, id=task_id)
        seconds = request.POST.get('seconds')
        if seconds is not None:
            task.duration = int(seconds)
            task.save()
            return JsonResponse({'status': 'success', 'duration': task.duration})
    return JsonResponse({'status': 'error'}, status=400)

def edit_task(request, pk):
    task = get_object_or_404(Task, id=pk)
    if request.method == 'POST':
        task.title = request.POST.get('title', task.title).strip()
        task.category = request.POST.get('category', task.category)
        task.save()
    return redirect('task_list')