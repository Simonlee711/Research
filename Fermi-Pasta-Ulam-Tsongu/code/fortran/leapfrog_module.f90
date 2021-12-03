! File: leapfrog_module.f90
! Author: Simon Lee
! Purpose: This holds and updates the solution depending on the physical parameters and initial conditions

module leapfrog
  use output
  implicit none
  real (dp), parameter :: pi = acos(-1.d0)

  
contains

  ! Function: Leap Frog Mechanism
  subroutine leapfrog_mechanism (N, alpha, runName)
    implicit none
    real (dp), allocatable :: xnp1(:) ! Rank 1 vector
    real (dp), allocatable :: x0(:) ! initial conditions as more rank 1 arrays
    real (dp), allocatable :: x1(:)
    real (dp), allocatable :: v0(:)
    real (dp), allocatable :: xnm1(:) ! initial conditions and time step variables as rank 1 arrays
    real (dp), allocatable :: xn(:)
    real (dp) :: C, K, dt ! variable that affect the M
    real (dp), intent(in) :: alpha  ! delta t and alpha 
    integer, intent(in) :: N ! number of masses
    character(len=maxStrLen) :: runName
    integer :: M
    real (dp) :: Tf
    !dt is an intent in variable, same with N which is the number of masses, alpha is intent in as well
    integer :: t, i, Num_mass  !loop iterators
    
    ! N is size 2 bigger
    Num_mass = N + 2
    ! allocate all arrays
    allocate(x0(Num_mass))
    allocate(x1(Num_mass))
    allocate(v0(Num_mass))
    allocate(xnm1(Num_mass))
    allocate(xn(Num_mass))
    allocate(xnp1(Num_mass)) 

    ! initial conditions x0 
    x0 = 0.0

    !initial conditions v0
    do i = 1, Num_mass
        v0(i) = sin((i*pi)/(Num_mass+1)) ! 
    end do 
    
    !initialize final time
    Tf = 10*pi
    K = 4*((Num_mass+1) ** 2)
    C = 0.5

    ! set M 
    if(alpha == 0.d0) then
        M = CEILING(Tf * SQRT(K))
    end if 
    if(alpha /= 0.d0) then 
        M = CEILING((Tf * SQRT(K))/C)
    end if

    !sets size of each step
    dt = Tf/M
    
    !initializing x1
    x1 = x0 + (dt * v0)

    !set x0 and x1 arrays to xn minus 1 and xn
    xnm1 = x0
    xn = x1


    do t = 1, M !time loop
        xnp1 = 0.0
        do i = 2, (Num_mass-1) ! space loop - start calculating from 2nd mass to 2nd to last mass
            !linear equation
            xnp1(i) = 2*xn(i) - xnm1(i) + K*(dt**2)*(xn(i+1) - 2*xn(i) + xn(i-1)) * (1 + alpha*(xn(i+1) - xn(i-1))) 


            !set the dummy variables
            xnp1(1) = 0 ! first element set to 0
            xnp1(Num_mass) = 0  ! last element set to 0 
        end do
        if ((t == CEILING(Tf/4)) .or. (t == CEILING(Tf/2)) .or. (t == CEILING((3*Tf)/4)) .or. (t == CEILING(Tf))) then
            call write_out(xnp1, Num_mass, runName)
        end if
        call write_out_N(xnp1,Num_mass, runName)
    
        xnm1 = xn ! xnm1 is now timestep 1 
        xn = xnp1 ! xn is now timestep 2
    end do
    
    deallocate(xnp1)
    deallocate(x0)
    deallocate(x1)
    deallocate(v0)
    deallocate(xnm1)
    deallocate(xn)

end subroutine leapfrog_mechanism

end module leapfrog