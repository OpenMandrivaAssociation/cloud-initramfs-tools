Summary:	Cloud image initramfs management utilities
Name:		cloud-initramfs-tools
Version:	0.20
Release:	1
License:	GPLv3
Group:		System Environment/Base
URL:		https://launchpad.net/ubuntu/saucy/+source/cloud-initramfs-tools
Source0:	https://launchpad.net/ubuntu/saucy/+source/cloud-initramfs-tools/%{version}ubuntu1/+files/cloud-initramfs-tools_%{version}ubuntu1.tar.gz
Patch0:		0000-strip-p-from-rootdisk.patch
Patch1:		0001-run-in-pre-mount-stage.patch
BuildArch:	noarch

%description
dracut-modules-growroot: Automatically resize the root partition on first boot

%package -n dracut-modules-growroot
Summary:	Automatically resize the root partition on first boot
Group:		System Environment/Base
Requires:	cloud-utils-growpart
Requires:	dracut
Requires:	grep
Requires:	util-linux

%description -n dracut-modules-growroot
This dracut module will re-write the partition table of a disk so that the
root partition has as much space as possible, bumping it up to the edge of the
disk, or the edge of the next partition.

%prep
%autosetup -p1 -n %{name}-%{version}ubuntu1

%build

%install
make install-fedora DESTDIR=$RPM_BUILD_ROOT%{_prefix}/lib/

%files -n dracut-modules-growroot
%doc COPYING README growroot/doc/example.txt
%dir %{_prefix}/lib/dracut/modules.d/50growroot
%{_prefix}/lib/dracut/modules.d/50growroot/growroot-dummy.sh
%{_prefix}/lib/dracut/modules.d/50growroot/growroot.sh
%{_prefix}/lib/dracut/modules.d/50growroot/module-setup.sh
