!this program reads three files and store their value in a new file
program read_xyz
    implicit none

    ! Declare variables
    integer :: i, num_lines
    integer :: every
    real :: t, x, y, z
    character(len=100) :: line
    character(len=20) :: file1, file2, file3

    every = 1000

    ! File name and unit number
    file1 = 'black_hole_1_x.t.asc'
    file2 = 'black_hole_1_y.t.asc'
    file3 = 'black_hole_1_z.t.asc'

    ! Open the file
    open(unit=1, file=file1, status='old', action='read')
    open(unit=2, file=file2, status='old', action='read')
    open(unit=3, file=file3, status='old', action='read')

    open(4,file='black_hole_1_xyz.t.asc')

    ! Count the number of lines in the file
    num_lines = 0
    do
        read(1, '(A)', iostat=i) line
        if (i /= 0) exit
        num_lines = num_lines + 1
    end do

    ! Rewind the file to the beginning
    rewind(1)
    rewind(2)
    rewind(3)

    ! Loop to read each line and store the values
    do i = 0, num_lines-1
        read(1, *) t, x
        read(2, *) t, y
        read(3, *) t, z
        
        if(mod(i,every).eq.0) then
            print *, i
            write(4,*) x, y, z
            write(4,*)
            write(4,*)
        end if

    end do

    ! Close the file
    close(4)
    close(3)
    close(2)
    close(1)

end program read_xyz

