Summary: Creates, views and edits BSD UNIX style disk labels on Alphas.
Name: minlabel
Version: 1.2
Release: 6
Copyright: GPL
ExclusiveArch: alpha
Group: System Environment/Base
Source: minlabel-1.2.tar.gz
BuildRoot: /var/tmp/%{name}-root

%description
Alpha machine's hard drives are partitioned in one of two ways:  PC style
partitioning or BSD UNIX style labeling.  The minlabel program allows
you to create, view and edit BSD UNIX style labels on Alpha hard drives.

%prep
%setup -q

%build
make RPM_OPT_FLAGS="$RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/sbin

install -m755 -s minlabel $RPM_BUILD_ROOT/sbin

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
/sbin/minlabel
