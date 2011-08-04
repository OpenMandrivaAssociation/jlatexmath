Summary:	An implementation of LaTeX math mode wrote in Java
Name:		jlatexmath
Version:	0.9.6
Release:	%mkrel 1
License:	GPLv2+
Group:		Development/Java
URL:		http://forge.scilab.org/index.php/p/jlatexmath/
Source0:	%{name}-src-all-%{version}.zip
BuildRequires:	ant >= 0:1.6
BuildRequires:	fop
BuildRequires:	java-rpmbuild
BuildRequires:	jpackage-utils >= 0:1.6
BuildRequires:	xalan-j2
BuildRequires:	xml-commons-apis
BuildRequires:	xml-commons-jaxp-1.3-apis
BuildRequires:	xmlgraphics-commons
Requires:	jpackage-utils
BuildArch:      noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot

%description
JLaTeXMath is an implementation of LaTeX math mode wrote in Java.

%prep
%setup -q

# remove all binary libs
find -type f -name "*.jar" -exec rm -rf {} \;

%build
export CLASSPATH=
export OPT_JAR_LIST=:
%ant minimal fop

%install
rm -rf %{buildroot}

# jars
mkdir -p %{buildroot}%{_javadir}
cp -p dist/jlatexmath{,-fop,-minimal}-%{version}.jar %{buildroot}%{_javadir}
cp -p dist/jlm_*.jar %{buildroot}%{_javadir}
pushd  %{buildroot}%{_javadir} 
    #create symlink
    ln -s %{name}-%{version}.jar %{name}.jar
    ln -s %{name}-fop-%{version}.jar %{name}-fop.jar
    ln -s %{name}-minimal-%{version}.jar %{name}-minimal.jar
popd

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_javadir}/*.jar
