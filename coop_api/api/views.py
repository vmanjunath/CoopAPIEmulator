from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from utils import fetch_member_dets
from models import UserData, Shift
import json
from django.forms.models import model_to_dict
from django.views.decorators.csrf import csrf_exempt


def index(request):
    return render(request, "api/index.html")


LIST_OF_IDS = "data/id_list.csv"


def reload_api(request):
    # start by clearing all existing data
    UserData.objects.all().delete()
    Shift.objects.all().delete()

    with open(LIST_OF_IDS, 'r') as id_list_file:
        lines = id_list_file.readlines()
        for line in lines:
            member_id = int(line)
            data = fetch_member_dets(member_id)

            ud = UserData.objects.create(member_id=member_id, generic_shift=json.dumps(data['genericShift']))

            for shift in data['nextShifts']:
                Shift.objects.create(user_data=ud, end=shift['end'], start=shift['start'],
                                     expiration=shift['expiration'], role=shift['role'], member=shift['member'],
                                     origShiftId=shift['origShiftId'], shiftId=shift['shiftId'])

    return HttpResponse("done.")


def shift_to_dict(shift):
    shift_dict = model_to_dict(shift)
    shift_dict.pop('id', None)
    shift_dict.pop('user_data', None)
    return shift_dict


def fetch(request, member_id):
    try:
        ud = UserData.objects.get(member_id=member_id)
    except UserData.DoesNotExist:
        return HttpResponse('')

    next_shifts = map(shift_to_dict, ud.shifts.all())
    gs = ud.generic_shift
    generic_shift = json.loads(gs)

    payload = {'nextShifts': next_shifts, 'genericShift': generic_shift}

    return JsonResponse(payload)


@csrf_exempt
def put(request):
    if request.method == 'POST':
        raw_data = request.read()
        data = json.loads(raw_data)

        for swap in data['swaps']:
            assign_new(swap['origShiftId'], swap['newShiftId'])

        return HttpResponse('[]')
    else:
        return HttpResponse('')


def assign_new(from_shift, to_shift):
    from_shift = Shift.objects.get(shiftId=from_shift)
    from_shift.shiftId = to_shift
    from_shift.save()