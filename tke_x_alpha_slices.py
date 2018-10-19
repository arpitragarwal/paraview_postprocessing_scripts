#### import the simple module from the paraview
import os
from paraview.simple import *
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

case_number = 8
# create a new 'OpenFOAMReader'
if case_number == 1:
    case_path = '/home/agarwal32/OpenFOAM/agarwal32-2.1.1/run/nozzle-internal-flow/cylindrical_nozzle/5p5_micron/'
    case_file_name = '5p5_micron.foam'
elif case_number == 2:
    case_path = '/home/agarwal32/OpenFOAM/agarwal32-2.1.1/run/nozzle-internal-flow/cylindrical_nozzle/4p4_micron/'
    case_file_name = '4p4_micron.foam'
elif case_number == 3:
    case_path = '/home/agarwal32/OpenFOAM/agarwal32-2.1.1/run/linear-stability-sprayA-nozzle/smooth_sprayA_576_nozzle/large_external_domain/v1_6Mcells/rho_715_u_412/original_case/'
    case_file_name = 'original_case.foam'
elif case_number == 4:
    case_path = '/home/agarwal32/OpenFOAM/agarwal32-2.1.1/run/linear-stability-sprayA-nozzle/smooth_sprayA_576_nozzle/large_external_domain/v6_15Mcells/original_case/'
    case_file_name = 'original_case.foam'
elif case_number == 5:
    case_path = '/home/agarwal32/OpenFOAM/agarwal32-2.1.1/run/linear-stability-sprayA-nozzle/smooth_sprayA_576_nozzle/large_external_domain/v7_x_max_4mm_22Mcells/original_case/'
    case_file_name = 'original_case.foam'
elif case_number == 6:
    case_path = '/home/agarwal32/OpenFOAM/agarwal32-2.1.1/run/nozzle-internal-flow/sprayA-rough-nozzle/rough-5p8mum-5p3Mcells/'
    case_file_name = 'rough-5p8mum-5p3Mcells.foam'
elif case_number == 7:
    case_path = '/home/agarwal32/OpenFOAM/agarwal32-2.1.1/run/nozzle-internal-flow/sprayA-rough-nozzle/rough-4p5mum-10p5Mcells/'
    case_file_name = 'rough-4p5mum-10p5Mcells.foam'
elif case_number == 8:
    case_path = '/home/agarwal32/OpenFOAM/agarwal32-2.1.1/run/nozzle-internal-flow/no-nozzle/flat_hat/5p5_micron/'
    case_file_name = '5p5_micron.foam'
elif case_number == 9:
    case_path = '/home/agarwal32/OpenFOAM/agarwal32-2.1.1/run/nozzle-internal-flow/no-nozzle/flat_hat/4micron_13Mcells/'
    case_file_name = '4micron_13Mcells.foam'

case_data = OpenFOAMReader(FileName=case_path + case_file_name)

case_data.MeshRegions = ['internalMesh']

# get animation scene
animationScene1 = GetAnimationScene()

# update animation scene based on data timesteps
animationScene1.UpdateAnimationUsingDataTimeSteps()

# Properties modified on case_data
case_data.CellArrays = ['alpha1', 'alpha1Mean', 'TKE']

# get active view
renderView1 = GetActiveViewOrCreate('RenderView')
# uncomment following to set a specific view size
# renderView1.ViewSize = [1437, 837]

# show data in view
case_dataDisplay = Show(case_data, renderView1)
# trace defaults for the display properties.
case_dataDisplay.Representation = 'Surface'
case_dataDisplay.ColorArrayName = [None, '']
case_dataDisplay.OSPRayScaleArray = 'alpha1'
case_dataDisplay.OSPRayScaleFunction = 'PiecewiseFunction'
case_dataDisplay.SelectOrientationVectors = 'None'
case_dataDisplay.ScaleFactor = 0.0008787387516349554
case_dataDisplay.SelectScaleArray = 'None'
case_dataDisplay.GlyphType = 'Arrow'
case_dataDisplay.GlyphTableIndexArray = 'None'
case_dataDisplay.DataAxesGrid = 'GridAxesRepresentation'
case_dataDisplay.PolarAxes = 'PolarAxesRepresentation'
case_dataDisplay.ScalarOpacityUnitDistance = 6.008416170441715e-05
case_dataDisplay.GaussianRadius = 0.0004393693758174777
case_dataDisplay.SetScaleArray = ['POINTS', 'alpha1']
case_dataDisplay.ScaleTransferFunction = 'PiecewiseFunction'
case_dataDisplay.OpacityArray = ['POINTS', 'alpha1']
case_dataDisplay.OpacityTransferFunction = 'PiecewiseFunction'

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
case_dataDisplay.OSPRayScaleFunction.Points = [-4.586513033601864e-23, 0.0, 0.5, 0.0, 1.0, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
case_dataDisplay.ScaleTransferFunction.Points = [-4.586513033601864e-23, 0.0, 0.5, 0.0, 1.0, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
case_dataDisplay.OpacityTransferFunction.Points = [-4.586513033601864e-23, 0.0, 0.5, 0.0, 1.0, 1.0, 0.5, 0.0]

# reset view to fit data
renderView1.ResetCamera()

# update the view to ensure updated data information
renderView1.Update()

view = GetActiveView()
reader = GetActiveSource()
tsteps = reader.TimestepValues
annTime = AnnotateTimeFilter(reader)
Show(annTime)
view.ViewTime = tsteps[-1]
Render()

# update the view to ensure updated data information
renderView1.Update()

# create a new 'Calculator'
calculator1 = Calculator(Input=case_data)
calculator1.Function = ''

# Properties modified on calculator1
calculator1.AttributeMode = 'Cell Data'
calculator1.ResultArrayName = 'tke_x_alpha1'
calculator1.Function = 'TKE*alpha1'

# create a new 'Calculator'
calculator2 = Calculator(Input=calculator1)
calculator2.Function = ''

# Properties modified on calculator2
calculator2.AttributeMode = 'Cell Data'
calculator2.ResultArrayName = 'tke_x_alpha1Mean'
calculator2.Function = 'TKE*alpha1Mean'


get_tke_data = True
integrated_tke = []
integrated_alpha1 = []
integrated_alpha1Mean = []
integrated_tke_x_alpha1 = []
integrated_tke_x_alpha1Mean = []

locations = []
for i in range (0, 25):
    slice_location = -0.5e-3 + (i) * 45e-6
    if case_number > 7:
        slice_location = 0 + (i) * 45e-6
    locations.append(slice_location)
    # create a new 'Slice'
    slice1 = Slice(Input=calculator2)
    slice1.SliceType = 'Plane'
    slice1.SliceOffsetValues = [0.0]

    # Properties modified on slice1.SliceType
    slice1.SliceType.Origin = [slice_location, 0.0, 0.0]

    # show data in view
    slice1Display = Show(slice1, renderView1)
    # trace defaults for the display properties.
    slice1Display.Representation = 'Surface'
    slice1Display.ColorArrayName = [None, '']
    slice1Display.OSPRayScaleArray = 'TKE'
    slice1Display.OSPRayScaleFunction = 'PiecewiseFunction'
    slice1Display.SelectOrientationVectors = 'None'
    slice1Display.ScaleFactor = 9.213012162945233e-06
    slice1Display.SelectScaleArray = 'None'
    slice1Display.GlyphType = 'Arrow'
    slice1Display.GlyphTableIndexArray = 'None'
    slice1Display.DataAxesGrid = 'GridAxesRepresentation'
    slice1Display.PolarAxes = 'PolarAxesRepresentation'
    slice1Display.GaussianRadius = 4.606506081472617e-06
    slice1Display.SetScaleArray = ['POINTS', 'TKE']
    slice1Display.ScaleTransferFunction = 'PiecewiseFunction'
    slice1Display.OpacityArray = ['POINTS', 'TKE']
    slice1Display.OpacityTransferFunction = 'PiecewiseFunction'

    # init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
    slice1Display.OSPRayScaleFunction.Points = [-4.586513033601864e-23, 0.0, 0.5, 0.0, 1.0, 1.0, 0.5, 0.0]

    # init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
    slice1Display.ScaleTransferFunction.Points = [-4.586513033601864e-23, 0.0, 0.5, 0.0, 1.0, 1.0, 0.5, 0.0]

    # init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
    slice1Display.OpacityTransferFunction.Points = [-4.586513033601864e-23, 0.0, 0.5, 0.0, 1.0, 1.0, 0.5, 0.0]

    # update the view to ensure updated data information
    renderView1.Update()

    # create a new 'Integrate Variables'
    integrateVariables1 = IntegrateVariables(Input=slice1)
    temp = integrateVariables1.GetCellDataInformation().GetArray('TKE').GetRange()
    integrated_tke.append(temp[0])
    temp = integrateVariables1.GetCellDataInformation().GetArray('alpha1').GetRange()
    integrated_alpha1.append(temp[0])
    temp = integrateVariables1.GetCellDataInformation().GetArray('alpha1Mean').GetRange()
    integrated_alpha1Mean.append(temp[0])
    temp = integrateVariables1.GetCellDataInformation().GetArray('tke_x_alpha1').GetRange()
    integrated_tke_x_alpha1.append(temp[0])
    temp = integrateVariables1.GetCellDataInformation().GetArray('tke_x_alpha1Mean').GetRange()
    integrated_tke_x_alpha1Mean.append(temp[0])

    # save data
    #os.chdir(case_path)
    #directory = './surface_disturbance_data/'
    #if not os.path.exists(directory):
    #    os.makedirs(directory)
    #SaveData(case_path + 'contour_data.csv', proxy=contour1, WriteAllTimeSteps=1)


# Create a new 'SpreadSheet View'
spreadSheetView1 = CreateView('SpreadSheetView')
spreadSheetView1.ColumnToSort = ''
spreadSheetView1.BlockSize = 1024L
# uncomment following to set a specific view size
# spreadSheetView1.ViewSize = [400, 400]

# get layout
layout1 = GetLayout()

# place view in the layout
layout1.AssignView(2, spreadSheetView1)

# show data in view
integrateVariables1Display = Show(integrateVariables1, spreadSheetView1)


# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
spreadSheetView1.Update()

#### saving camera placements for all active views

# current camera placement for renderView1
renderView1.CameraPosition = [0.002606480149552226, 0.0, 0.0201892992903625]
renderView1.CameraFocalPoint = [0.002606480149552226, 0.0, 0.0]
renderView1.CameraParallelScale = 0.005225375163620621
