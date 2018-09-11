#### import the simple module from the paraview
from paraview.simple import *
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

# create a new 'OpenFOAMReader'
#case_data = OpenFOAMReader(FileName='/home/agarwal32/OpenFOAM/agarwal32-2.1.1/run/nozzle-internal-flow/cylindrical_nozzle/5p5_micron/5p5_micron.foam')

#case_data = OpenFOAMReader(FileName='/home/agarwal32/OpenFOAM/agarwal32-2.1.1/run/linear-stability-sprayA-nozzle/smooth_sprayA_576_nozzle/large_external_domain/v1_6Mcells/rho_715_u_412/original_case/original_case.foam')
#case_data = OpenFOAMReader(FileName='/home/agarwal32/OpenFOAM/agarwal32-2.1.1/run/linear-stability-sprayA-nozzle/smooth_sprayA_576_nozzle/large_external_domain/v6_15Mcells/original_case/original_case.foam')
case_data = OpenFOAMReader(FileName='/home/agarwal32/OpenFOAM/agarwal32-2.1.1/run/linear-stability-sprayA-nozzle/smooth_sprayA_576_nozzle/large_external_domain/v7_x_max_4mm_22Mcells/original_case/original_case.foam')

#case_data = OpenFOAMReader(FileName='/home/agarwal32/OpenFOAM/agarwal32-2.1.1/run/nozzle-internal-flow/sprayA-rough-nozzle/rough-5p8mum-5p3Mcells/rough-5p8mum-5p3Mcells.foam')
#case_data = OpenFOAMReader(FileName='/home/agarwal32/OpenFOAM/agarwal32-2.1.1/run/nozzle-internal-flow/sprayA-rough-nozzle/rough-4p5mum-10p5Mcells/rough-4p5mum-10p5Mcells.foam')

case_data.MeshRegions = ['internalMesh']
case_data.CellArrays = ['TKE', 'U', 'UMean', 'UPrime2Mean', 'alpha1', 'alpha1Mean', 'beta', 'beta_Filtered', 'p_rgh']

# get animation scene
animationScene1 = GetAnimationScene()

# update animation scene based on data timesteps
animationScene1.UpdateAnimationUsingDataTimeSteps()

# Properties modified on case_data
case_data.CellArrays = ['alpha1']

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


# create a new 'Contour'
contour1 = Contour(Input=case_data)
contour1.ContourBy = ['POINTS', 'alpha1']
contour1.Isosurfaces = [0.5]
contour1.PointMergeMethod = 'Uniform Binning'

# show data in view
contour1Display = Show(contour1, renderView1)
# trace defaults for the display properties.
contour1Display.Representation = 'Surface'
contour1Display.ColorArrayName = [None, '']
contour1Display.OSPRayScaleArray = 'Normals'
contour1Display.OSPRayScaleFunction = 'PiecewiseFunction'
contour1Display.SelectOrientationVectors = 'None'
contour1Display.ScaleFactor = 0.0001574089525092859
contour1Display.SelectScaleArray = 'None'
contour1Display.GlyphType = 'Arrow'
contour1Display.GlyphTableIndexArray = 'None'
contour1Display.DataAxesGrid = 'GridAxesRepresentation'
contour1Display.PolarAxes = 'PolarAxesRepresentation'
contour1Display.GaussianRadius = 7.870447625464295e-05
contour1Display.SetScaleArray = [None, '']
contour1Display.ScaleTransferFunction = 'PiecewiseFunction'
contour1Display.OpacityArray = [None, '']
contour1Display.OpacityTransferFunction = 'PiecewiseFunction'

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
contour1Display.OSPRayScaleFunction.Points = [-4.586513033601864e-23, 0.0, 0.5, 0.0, 1.0, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
contour1Display.ScaleTransferFunction.Points = [-4.586513033601864e-23, 0.0, 0.5, 0.0, 1.0, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
contour1Display.OpacityTransferFunction.Points = [-4.586513033601864e-23, 0.0, 0.5, 0.0, 1.0, 1.0, 0.5, 0.0]

# hide data in view
Hide(case_data, renderView1)

# update the view to ensure updated data information
renderView1.Update()

perimeter = []
locations = []
#f = open("perimeter_data.txt", "wb")
#writer = CreateWriter("foo.csv")
for i in range (0, 40):
    slice_location = (i + 0.5) * 90e-6
    locations.append(slice_location)
    # create a new 'Slice'
    slice1 = Slice(Input=contour1)
    slice1.SliceType = 'Plane'
    slice1.SliceOffsetValues = [0.0]

    # init the 'Plane' selected for 'SliceType'
    slice1.SliceType.Origin = [0.0007855645344534423, -3.902277967426926e-06, 1.3375392882153392e-06]

    # Properties modified on slice1.SliceType
    slice1.SliceType.Origin = [slice_location, -3.902277967426926e-06, 1.3375392882153392e-06]

    # show data in view
    slice1Display = Show(slice1, renderView1)
    # trace defaults for the display properties.
    slice1Display.Representation = 'Surface'
    slice1Display.ColorArrayName = [None, '']
    slice1Display.OSPRayScaleArray = 'Normals'
    slice1Display.OSPRayScaleFunction = 'PiecewiseFunction'
    slice1Display.SelectOrientationVectors = 'None'
    slice1Display.ScaleFactor = 8.952260759542697e-06
    slice1Display.SelectScaleArray = 'None'
    slice1Display.GlyphType = 'Arrow'
    slice1Display.GlyphTableIndexArray = 'None'
    slice1Display.DataAxesGrid = 'GridAxesRepresentation'
    slice1Display.PolarAxes = 'PolarAxesRepresentation'
    slice1Display.GaussianRadius = 4.4761303797713484e-06
    slice1Display.SetScaleArray = [None, '']
    slice1Display.ScaleTransferFunction = 'PiecewiseFunction'
    slice1Display.OpacityArray = [None, '']
    slice1Display.OpacityTransferFunction = 'PiecewiseFunction'

    # init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
    slice1Display.OSPRayScaleFunction.Points = [-4.586513033601864e-23, 0.0, 0.5, 0.0, 1.0, 1.0, 0.5, 0.0]

    # init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
    slice1Display.ScaleTransferFunction.Points = [-4.586513033601864e-23, 0.0, 0.5, 0.0, 1.0, 1.0, 0.5, 0.0]

    # init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
    slice1Display.OpacityTransferFunction.Points = [-4.586513033601864e-23, 0.0, 0.5, 0.0, 1.0, 1.0, 0.5, 0.0]

    # hide data in view
    Hide(contour1, renderView1)

    # update the view to ensure updated data information
    renderView1.Update()

    # create a new 'Integrate Variables'
    integrateVariables1 = IntegrateVariables(Input=slice1)
    temp = integrateVariables1.GetCellDataInformation().GetArray('Length').GetRange()
    perimeter.append(temp[0])
    #f.write('%d,   ', slice_location)
    #f.write('%d\n'  , temp[0])

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


