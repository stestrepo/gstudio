''' -- imports from installed packages -- '''
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect,HttpResponse,StreamingHttpResponse
from django.core.urlresolvers import reverse
from django.shortcuts import render_to_response, render
from django.template import RequestContext

try:
  from bson import ObjectId
except ImportError:  # old pymongo
  from pymongo.objectid import ObjectId

from gnowsys_ndf.settings import *
from gnowsys_ndf.ndf.models import *
from gnowsys_ndf.ndf.views.methods import *


def type_created(request,group_id):
    print "\n\n\n\n\n", "type_created" ,group_id , "\n\n\n\n\n\n\n\n"

    try:
        group_id = ObjectId(group_id)
    except:
        group_name, group_id = get_group_name_id(group_id)


    option_list = []
    opt_list = []
    newdict = {}
    
    # option_list = ['_type','name','altnames','plural','language','type_of','member_of','access_policy',
    # 'created_at','created_by','last_update','modified_by','contributors','location','content','group_set',
    # 'collection_set','property_order','login_required','status','meta_type_set','attribute_type_set',
    # 'relation_type_set','process_type_set']
        

    gst = node_collection.find({'_type':'GSystemType'})

    for e in gst :
        option_list.append(e.name)
        # opt_list.append(e)

    class_name="GSystemType"

    class_structure = eval(class_name).structure

    # if node_id:
    #     new_instance_type = node_collection.one({'_type': unicode(class_name), '_id': ObjectId(node_id)})
    # else:

    new_instance_type = eval("node_collection.collection"+"."+class_name)()



    if request.method=="POST":
        for key,value in class_structure.items():
            if request.POST.get(key,""):
                new_instance_type[key] = request.POST.get(key,"")

            new_instance_type.save()


    # If GET request ---------------------------------------------------------------------------------------
    for key,value in class_structure.items():

            newdict[key] = [value, new_instance_type[key]]

    class_structure = newdict

    no_page_gst = []

    no_page_gst = [ u'Twist', u'Reply', u'Author', u'Shelf', u'Pandora_video', u'task_update_history',
     u'Theme',  u'theme_item', u'Concept', u'article', u'book', u'conference', u'inbook', u'incollection',
     u'inproceedings',
     u'manual',
     u'masterthesis',
     u'misc',
     u'phdthesis',
     u'proceedings',
     u'techreport',
     u'unpublished_entry',
     u'booklet',
     u'GList',
     u'GListItem',
     u'CourseEventGroup',
     u'PartnerGroup',
     u'ModeratingGroup',
     u'Info page',
     u'Blog page',
     u'Wiki page',
     u'Place',
     u'Country',
     u'Caste',
     u'Enrollment',
     u'MIS-PO',
     u'CourseSection',
     u'CourseUnit',
     u'CourseSectionEvent',
     u'CourseUnitEvent',
     u'State',
     u'District',
     u'StudentCourseEnrollment',
     u'MIS',
     u'CourseSubSectionEvent',
     u'CourseSubSection',
     u'Inauguration',
     u'Field Visit',
     u'Meeting',
     u'Orientation',
     u'Master Trainer Program',
     u'Training of Teachers',
     u'Course Developers Meeting',
     u'Session',
     u'Classroom Session',
     u'Lab Session',
     u'Exam',
     u'NUSSD Course',
     u'Announced Course',
     u'College',
     u'Organization',
     u'Person',
     u'Student',
     u'Voluntary Teacher',
     u'NSS Coordinator',
     u'Course Developer',
     u'Steering Committee Member',
     u'Program Officer',
     u'Program Manager',
     u'Partners',
     u'Master Trainer',
     u'University',
     u'Faculty Coordinator'
     u'Batch',      
     'Module',
     'WikiData',
      'Topic',
      'Topics',
     'Bib_App', 
     'Event',
     'Observation', 
      ]
      

    opt_list = ['Page', 'File', 'Group', 'Image', 'Video', 'Forum', 'Course', 'Task',
      'E-Book', 'ProgramEventGroup', 'QuizItem', 'Quiz']




    template = "ndf/type_created.html"
    variable = RequestContext(request, {'group_id':group_id,'groupid':group_id,'option_list':option_list,'opt_list':opt_list })

    return render_to_response(template,variable)


    # return render(request,"ndf/type_create.html" )
    # return HttpResponse( template , context )
    # return render_to_response ( template , variable )