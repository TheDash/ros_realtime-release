Name:           ros-hydro-rosrt
Version:        1.0.24
Release:        0%{?dist}
Summary:        ROS rosrt package

Group:          Development/Libraries
License:        BSD
URL:            http://ros.org/wiki/rosrt
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-hydro-allocators
Requires:       ros-hydro-lockfree
Requires:       ros-hydro-rosatomic
Requires:       ros-hydro-roscpp
Requires:       ros-hydro-roslib
Requires:       ros-hydro-rosunit
Requires:       ros-hydro-std-msgs
BuildRequires:  ros-hydro-allocators
BuildRequires:  ros-hydro-catkin
BuildRequires:  ros-hydro-lockfree
BuildRequires:  ros-hydro-rosatomic
BuildRequires:  ros-hydro-roscpp
BuildRequires:  ros-hydro-roslib
BuildRequires:  ros-hydro-rosunit
BuildRequires:  ros-hydro-std-msgs

%description
rosrt provides classes for interfacing with ROS from within realtime systems,
such as realtime-safe Publisher and Subscriber classes.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/hydro/setup.sh" ]; then . "/opt/ros/hydro/setup.sh"; fi
mkdir -p build && cd build
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/hydro" \
        -DCMAKE_PREFIX_PATH="/opt/ros/hydro" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/hydro/setup.sh" ]; then . "/opt/ros/hydro/setup.sh"; fi
cd build
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/hydro

%changelog
* Thu Nov 06 2014 Devon Ash <dash@clearpathrobotics.com> - 1.0.24-0
- Autogenerated by Bloom

* Mon Nov 03 2014 Devon Ash <dash@clearpathrobotics.com> - 1.0.23-0
- Autogenerated by Bloom

* Wed Oct 29 2014 Devon Ash <dash@clearpathrobotics.com> - 1.0.22-0
- Autogenerated by Bloom

* Mon Oct 27 2014 Devon Ash <dash@clearpathrobotics.com> - 1.0.17-0
- Autogenerated by Bloom

* Mon Oct 27 2014 Devon Ash <dash@clearpathrobotics.com> - 1.0.21-0
- Autogenerated by Bloom

* Fri Oct 24 2014 Devon Ash <dash@clearpathrobotics.com> - 1.0.16-0
- Autogenerated by Bloom

* Wed Oct 22 2014 Devon Ash <dash@clearpathrobotics.com> - 1.0.14-0
- Autogenerated by Bloom

* Wed Oct 22 2014 Devon Ash <dash@clearpathrobotics.com> - 1.0.15-0
- Autogenerated by Bloom

* Fri Oct 17 2014 Devon Ash <dash@clearpathrobotics.com> - 1.0.13-0
- Autogenerated by Bloom

* Tue Oct 14 2014 Devon Ash <dash@clearpathrobotics.com> - 1.0.12-0
- Autogenerated by Bloom

* Thu Oct 09 2014 Devon Ash <dash@clearpathrobotics.com> - 1.0.10-0
- Autogenerated by Bloom

* Thu Sep 18 2014 Devon Ash <dash@clearpathrobotics.com> - 1.0.9-0
- Autogenerated by Bloom

* Wed Sep 10 2014 Devon Ash <dash@clearpathrobotics.com> - 1.0.7-0
- Autogenerated by Bloom

* Wed Sep 10 2014 Devon Ash <dash@clearpathrobotics.com> - 1.0.7-1
- Autogenerated by Bloom

* Wed Sep 10 2014 Devon Ash <dash@clearpathrobotics.com> - 1.0.4-0
- Autogenerated by Bloom

* Mon Sep 08 2014 Devon Ash <dash@clearpathrobotics.com> - 1.0.3-0
- Autogenerated by Bloom

