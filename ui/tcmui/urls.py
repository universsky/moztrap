from django.conf.urls.defaults import patterns, url, include
from django.conf import settings



urlpatterns = patterns(
    "",
    url("^account/", include("tcmui.users.urls")),

    # run tests
    url("^$", "tcmui.testexecution.views.picker", name="runtests"),
    url("^environment/$",
        "tcmui.environments.views.set_environment",
        name="environment"),
    url("^run/(?P<testrun_id>\d+)/$",
        "tcmui.testexecution.views.runtests",
        name="runtests_run"),

    # runtests ajax
    url("^runtests/_picker/cycles/(?P<parent_id>\d+)/",
        "tcmui.testexecution.views.picker_cycles",
        name="runtests_picker_cycles"),
    url("^runtests/_picker/runs/(?P<parent_id>\d+)/",
        "tcmui.testexecution.views.picker_runs",
        name="runtests_picker_runs"),
    url("^runtests/_picker/environments/(?P<parent_id>\d+)/",
        "tcmui.testexecution.views.picker_environments",
        name="runtests_picker_environments"),
    url("^_result/(?P<result_id>\d+)/$",
        "tcmui.testexecution.views.result",
        name="result"),

    # manage
    url("^manage/", include("tcmui.manage.urls")),

    # results
    url("^results/", include("tcmui.results.urls")),
)

if settings.DEBUG:
    urlpatterns += patterns(
        "",
        url("^debug/", include("tcmui.debug.urls")))
